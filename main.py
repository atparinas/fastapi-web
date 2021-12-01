from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from infrastructure import db_session
from views import home, account, packages

app = FastAPI()

app.mount('/static', StaticFiles(directory="static"), name="static")
app.include_router(home.router)
app.include_router(account.router)
app.include_router(packages.router)

file = (Path(__file__).parent / 'db' / 'pypi.sqlite').absolute()
db_session.global_init(file.as_posix())


