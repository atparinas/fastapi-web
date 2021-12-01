from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from viewmodels.package.details_viewmodel import DetailsViewModel

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/projects/{package_name}", response_class=HTMLResponse)
def details(request: Request, package_name: str):
    vm = DetailsViewModel(request, package_name=package_name)

    return templates.TemplateResponse("packages/details.html", context=vm.to_dict())
