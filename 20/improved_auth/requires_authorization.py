import hashlib
import os
from .models import User

def create_salt():
    return os.urandom(16).hex()

def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

def ok_user_and_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user:
        hashed_password = hash_password(password, user.salt)
        return hashed_password == user.password_hash
    return False
