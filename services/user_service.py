from typing import Optional

from infrastructure import db_session
from models.user import User
from passlib.handlers.sha2_crypt import sha512_crypt as crypto

def user_count() -> int:
    session = db_session.create_session()

    try:
        return session.query(User).count()
    finally:
        session.close()


def create_account(name: str, email: str, password: str):
    session = db_session.create_session()

    custom_crypt = crypto.using(rounds=214214)

    try:
        user = User()
        user.email = email
        user.name = name
        user.hashed_password = custom_crypt.hash(password)

        session.add(user)
        session.commit()

        return user
    finally:
        session.close()


def login_user(email: str, password: str):
    session = db_session.create_session()
    try:
        user = session.query(User).filter(User.email == email).first()
        if not user:
            return None
        if not crypto.verify(secret=password, hash=user.hashed_password):
            return None

        return user

    finally:
        session.close()


def get_user_by_id(id: int) -> Optional[User]:
    session = db_session.create_session()
    try:
        user = session.query(User).filter(User.id == id).first()
        return user
    finally:
        session.close()