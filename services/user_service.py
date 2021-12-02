from infrastructure import db_session
from models.user import User


def login_user(email: str, password: str):
    # TODO: check if email and password match for user

    return User('Andy', email, password)


def user_count() -> int:
    session = db_session.create_session()

    try:
        return session.query(User).count()
    finally:
        session.close()


def create_account(name: str, email: str, password: str):
    return User(name, email, password)
