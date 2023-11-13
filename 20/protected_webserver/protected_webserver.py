from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    current_user,
)

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:///test.db"  # In-memory database # noqa.
app.config["SECRET_KEY"] = "test"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
auth = HTTPBasicAuth()
login_manager = LoginManager(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def home():
    return "Welcome to the Flask Webserver! It's up and running."


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        login_user(user)
        return True
    return False


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        login_user(user)
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401


@app.route("/protected")
@login_required
def protected():
    if not current_user.is_authenticated:
        abort(403)
    return f"Hello, {current_user.username}! This is protected data."


def setup_database(app):
    with app.app_context():
        db.create_all()


# Add other routes and logic as needed
if __name__ == "__main__":
    setup_database(app)  # Create database tables
    app.run(debug=True)  # Use HTTPS
