from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from viewmodels.account.account_viewmodel import AccountViewModel
from viewmodels.account.register_viewmodel import RegisterViewModel

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get('/account')
def index(request: Request):
    vm = AccountViewModel(request)
    return templates.TemplateResponse("account/index.html", vm.to_dict())


@router.get('/account/register')
def register(request: Request):
    vm = RegisterViewModel(request)
    return templates.TemplateResponse("account/register.html", vm.to_dict())


@router.post('/account/register')
def register(request: Request):
    vm = RegisterViewModel(request)
    return templates.TemplateResponse("account/register.html", vm.to_dict())


@router.get('/account/login')
def login(request: Request):
    return templates.TemplateResponse("account/login.html", {"request": request})


@router.get('/account/logout')
def logout(request: Request):
    pass
