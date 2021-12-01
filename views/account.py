
from starlette import status
from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from viewmodels.account.account_viewmodel import AccountViewModel
from viewmodels.account.login_viewmodel import LoginViewModel
from viewmodels.account.register_viewmodel import RegisterViewModel
from services import user_service
from infrastructure import cookie_auth

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
async def register(request: Request):
    vm = RegisterViewModel(request)
    await vm.load()

    if vm.error:
         return templates.TemplateResponse("account/register.html", vm.to_dict())

    account = user_service.create_account(name=vm.name, email=vm.email, password=vm.password)

    response = RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, account.id )

    return response


@router.get('/account/login')
def login(request: Request):
    vm = LoginViewModel(request)
    return templates.TemplateResponse("account/login.html", vm.to_dict())


@router.post('/account/login')
def login(request: Request):
    vm = LoginViewModel(request)
    vm.load()

    if vm.error:
        return templates.TemplateResponse("account/login.html", vm.to_dict())

    user = user_service.login_user(vm.email, vm.password)

    if not user:
        vm.error = "The account does not exist or the password is wrong"
        return templates.TemplateResponse("account/login.html", vm.to_dict())

    response = RedirectResponse('/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, user.id)

    return response


@router.get('/account/logout')
def logout(request: Request):
    response = RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.logout(response)

    return response

