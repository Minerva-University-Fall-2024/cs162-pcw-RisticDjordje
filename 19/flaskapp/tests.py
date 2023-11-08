import unittest
from server import app, db, User, Expression
from werkzeug.security import generate_password_hash

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        # Configure the app for testing mode
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        
        # Create the database and the database table
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Drop the database tables and close the session
        with app.app_context():
            db.drop_all()

    def test_register(self):
        # Test that a user can register
        response = self.app.post('/register', data=dict(email='test@example.com', password='securepassword'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Check the user was inserted into the database
        with app.app_context():
            user = User.query.filter_by(email='test@example.com').first()
            self.assertIsNotNone(user)

    def test_login_logout(self):
        # Register a user
        hashed_password = generate_password_hash('mypassword')
        user = User(email='user@example.com', password_hash=hashed_password)
        with app.app_context():
            db.session.add(user)
            db.session.commit()

        # Test that the user can login
        response = self.app.post('/login', data=dict(email='user@example.com', password='mypassword'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        with self.app as client:
            with client.session_transaction() as sess:
                self.assertTrue(sess['user_id'])

        # Test that the user can logout
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        with self.app as client:
            with client.session_transaction() as sess:
                self.assertNotIn('user_id', sess)

    def test_dashboard_access(self):
        # Test that the dashboard is inaccessible without login and redirects to login page
        response = self.app.get('/dashboard', follow_redirects=True)
        self.assertIn(b'<!-- HTML form for login -->', response.data)

        # Register and login a user to access the dashboard
        self.test_register()
        self.app.post('/login', data=dict(email='test@example.com', password='securepassword'), follow_redirects=True)

        # Test that the dashboard is accessible after login
        response = self.app.get('/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<!-- HTML to display the dashboard and history -->', response.data)

    def test_expression_evaluation(self):
        # Test that expression evaluation is inaccessible without login and redirects to login page
        response = self.app.post('/evaluate', data=dict(expression='2+2'), follow_redirects=True)
        self.assertIn(b'<!-- HTML form for login -->', response.data)

        # Register and login a user
        self.test_register()
        self.app.post('/login', data=dict(email='test@example.com', password='securepassword'), follow_redirects=True)

        # Test that an expression can be evaluated after login
        response = self.app.post('/evaluate', data=dict(expression='2+2'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Check that the expression was saved to the database
        with app.app_context():
            expression = Expression.query.first()
            self.assertIsNotNone(expression)
            self.assertEqual(expression.content, '2+2')
            # The result is not tested here because safe_evaluate needs to be implemented

if __name__ == 'main':
    unittest.main()