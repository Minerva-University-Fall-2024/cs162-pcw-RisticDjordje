from flask import Flask, request, jsonify
import sqlite3
import hashlib
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Connect to the SQLite Database
def get_db_connection():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn


# Initialize the database with the users table
def init_db():
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            userid INT PRIMARY KEY,
            username TEXT,
            email TEXT,
            password TEXT
        );
    """
    )
    conn.commit()
    conn.close()


# Hash a password before storing it
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


@app.route("/")
def index():
    users = [
        (1, "cs162_user", "cs162@minerva.kgi.edu", "longpasswordsaresecure"),
        (2, "admin", "admin@minerva.kgi.edu", "123456"),
        (3, "prof_smith", "smith@minerva.kgi.edu", "password123"),
    ]

    conn = get_db_connection()

    for user in users:
        userid, username, email, password = user
        hashed_password = hash_password(password)
        conn.execute(
            "INSERT OR IGNORE INTO users (userid, username, email, password) VALUES (?, ?, ?, ?)",# noqa 
            (userid, username, email, hashed_password),
        )

    conn.commit()
    conn.close()

    return "Welcome to the Flask Webserver! Go to the login page at http://127.0.0.1:5000/login"


@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    email = request.form["email"]
    password = hash_password(request.form["password"])

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
        (username, email, password),
    )
    conn.commit()
    conn.close()
    return jsonify({"status": "success", "message": "User registered."})


@app.route("/login", methods=["GET"])
def show_login_form():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = hash_password(request.form["password"])

    conn = get_db_connection()
    # Intentionally vulnerable to SQL injection
    query = (
        f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    )
    user = conn.execute(query).fetchone()
    conn.close()

    if user:
        return jsonify({"status": "success", "message": "Login successful."})
    else:
        return jsonify({"status": "fail", "message": "Invalid username or password."})


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
