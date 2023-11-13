import unittest
from protected_webserver.protected_webserver import app, db, User
from flask_bcrypt import Bcrypt


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        print("Setting up the test environment...")
        self.app = app.test_client()
        app.config["TESTING"] = True

        with app.app_context():
            app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
            db.create_all()

            bcrypt = Bcrypt(app)
            hashed_password = bcrypt.generate_password_hash("testpassword").decode(
                "utf-8"
            )
            test_user = User(username="testuser", password_hash=hashed_password)
            db.session.add(test_user)
            db.session.commit()
        print("Test environment setup complete.")

    def tearDown(self):
        print("Tearing down the test environment...")
        with app.app_context():
            db.session.remove()
            db.drop_all()
        print("Test environment teardown complete.")

    def test_protected_route_unauthorized(self):
        print("Testing unauthorized access to protected route...")
        response = self.app.get("/protected")
        self.assertEqual(response.status_code, 401)
        print("Unauthorized access test passed.")

    def test_protected_route_authorized(self):
        print("Testing authorized access to protected route...")

        print("Attempting to log in...")
        login_response = self.app.post(
            "/login",
            data=dict(username="testuser", password="testpassword"),
            follow_redirects=True,
        )

        self.assertEqual(login_response.status_code, 200, "Login failed")
        print("Login successful.")

        print("Accessing protected route...")
        protected_response = self.app.get("/protected")
        self.assertEqual(
            protected_response.status_code,
            200,
            "Access to protected route unauthorized",
        )
        print("Authorized access test passed.")

    # Add more tests as needed


if __name__ == "__main__":
    unittest.main()
