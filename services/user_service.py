
from models.user import User

def login_user(email: str, password: str):
    # TODO: check if email and password match for user

    return User('Andy', email, password)

def user_count() -> int:
    pass

def create_account(name: str, email: str, password: str):
    return User(name, email, password)

