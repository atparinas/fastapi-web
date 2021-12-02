import hashlib

from starlette import requests
from starlette.responses import Response
from starlette.requests import Request
from typing import Optional

auth_key = 'pypiaccount'


def set_auth(response: Response, user_id: int):
    hash_val = __hash_text(str(user_id))
    val = "{}:{}".format(user_id, hash_val)
    response.set_cookie(auth_key, val, secure=False, httponly=True, samesite='Lax')


def __hash_text(text: str) -> str:
    text = 'salty__' + text + '__text'
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def get_user_id_from_auth_cookie(request: Request) -> Optional[int]:

    if auth_key not in request.cookies:
        print("No Authkey")
        return None

    val = request.cookies[auth_key]
    parts = val.split(':')
    if len(parts) != 2:
        return None

    user_id = parts[0]
    hash_val = parts[1]
    hash_val_check = __hash_text(user_id)

    if hash_val != hash_val_check:
        return None

    return int(user_id)


def logout(response: Response):
    response.delete_cookie(auth_key)
