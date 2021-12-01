from typing import Optional
from starlette.requests import Request


class ViewModelBase:

    def __init__(self, request: Request):
        self.request: Request = request
        self.error: Optional[str] = None
        self.user_id: Optional[int] = None

        self.is_logged_in = False

    def to_dict(self):
        return self.__dict__