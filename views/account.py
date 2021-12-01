
from starlette import status
from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from viewmodels.account.account_viewmodel import AccountViewModel
from viewmodels.account.register_viewmodel import RegisterViewModel
from services import user_service

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

    # TODO: Create Account
    # user_service.create_account(name=vm.name, email=vm.email, password=vm.password)

    # TODO: Login the user

    print("Redirecting")
    return RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)


@router.get('/account/login')
def login(request: Request):
    return templates.TemplateResponse("account/login.html", {"request": request})


@router.get('/account/logout')
def logout(request: Request):
    pass
