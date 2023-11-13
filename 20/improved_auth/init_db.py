from runserver import db
from .models import User
from .requires_authorization import create_salt, hash_password

def init_db():
    db.create_all()
    users = [
        User(username="Booker", password_hash="", salt=""),
        # Add other users here
    ]
    for user in users:
        user.salt = create_salt()
        user.password_hash = hash_password("password", user.salt)
        db.session.add(user)
    db.session.commit()

if __name__ == "__main__":
    init_db()
