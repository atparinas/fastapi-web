import datetime
from typing import List

from starlette.requests import Request

from models.release import Release
from services import package_service
from viewmodels.shared.viewmodel import ViewModelBase


class DetailsViewModel(ViewModelBase):

    def __init__(self, request: Request, package_name: str):
        super().__init__(request)
        self.request = request
        self.package_name = package_name
        self.package = package_service.get_package_by_id(package_name)
        self.latest_release = package_service.get_latest_release_for_package(package_name)
        self.latest_version = '0.0.0'
        self.is_latest = True
        self.release_version = self.latest_release.version






