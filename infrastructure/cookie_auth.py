from starlette import requests
from starlette.responses import Response
from starlette.requests import Request
from typing import Optional

auth_key = 'pypiaccount'

def set_auth(response: Response, user_id: int):
    response.set_cookie(auth_key, str(user_id), secure=False, httponly=True)




def get_user_id_from_auth_cookie(request: Request) -> Optional[int]:
    
    if auth_key not in request.cookies:
        return None

    user_id = int(request.cookies[auth_key])
    return user_id