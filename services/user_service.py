
from models.user import User



def user_count() -> int:
    pass

def create_account(name: str, email: str, password: str):
    return User(name, email, password)

