from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from viewmodels.home.index_viewmodel import IndexViewModel

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def index(request: Request):

    vm = IndexViewModel(request)
    context = vm.to_dict()

    return templates.TemplateResponse("home/index.html", context=context)
