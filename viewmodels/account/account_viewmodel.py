from starlette.requests import Request

from models.user import User
from viewmodels.shared.viewmodel import ViewModelBase


class AccountViewModel(ViewModelBase):

    def __init__(self, request: Request):
        super().__init__(request)
        self.user = User(name="Andy Parinas", email="atparinas@gmail.com", hashed_password="asdasdasdasda")


