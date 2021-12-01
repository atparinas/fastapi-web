from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from views import home, account, packages

app = FastAPI()

app.mount('/static', StaticFiles(directory="static"), name="static")
app.include_router(home.router)
app.include_router(account.router)
app.include_router(packages.router)
