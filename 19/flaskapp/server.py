from flask import Flask, request, session, redirect, url_for, render_template_string
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "your_secret_key"

db = SQLAlchemy(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    expressions = db.relationship("Expression", backref="user", lazy=True)


class Expression(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(120), nullable=False)
    result = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


# Registration endpoint
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        # Add new user after hashing the password
        hashed_password = generate_password_hash(password)
        new_user = User(email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template_string("<!-- HTML form for registration -->")


# Login endpoint
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            session["user_id"] = user.id
            return redirect(url_for("dashboard"))
        else:
            return "Invalid credentials", 401
    return render_template_string("<!-- HTML form for login -->")


# Dashboard endpoint
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    user_id = session["user_id"]
    user = User.query.get(user_id)
    expressions = Expression.query.filter_by(user_id=user.id).all()
    return render_template_string(
        "<!-- HTML to display the dashboard and history -->", expressions=expressions
    )


# Expression evaluation endpoint
@app.route("/evaluate", methods=["POST"])
def evaluate():
    if "user_id" not in session:
        return redirect(url_for("login"))
    expression = request.form["expression"]
    # Evaluate the expression using a safe method
    result = str(
        safe_evaluate(expression)
    )  # Implement safe_evaluate to parse and evaluate the expression
    new_expression = Expression(
        content=expression, result=result, user_id=session["user_id"]
    )
    db.session.add(new_expression)
    db.session.commit()
    return redirect(url_for("dashboard"))


# Logout endpoint
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login"))


if __name__ == "main":
    with app.app_context():
        db.create_all()
    app.run(debug=True)