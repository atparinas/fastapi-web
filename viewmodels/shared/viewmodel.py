from typing import Optional
from starlette.requests import Request

from infrastructure import cookie_auth


class ViewModelBase:

    def __init__(self, request: Request):
        self.request: Request = request
        self.error: Optional[str] = None
        self.user_id = cookie_auth.get_user_id_from_auth_cookie(self.request)
        self.is_logged_in = self.user_id is not None

    def to_dict(self):
        return self.__dict__
