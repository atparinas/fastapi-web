from datetime import datetime
from typing import List, Optional

from models.package import Package
from models.release import Release


def release_count():
    return 0


def package_count():
    return 0


def latest_releases(limit: int = 10) -> List:
    return []


def get_package_by_id(package_name: str) -> Optional[Package]:
    package = Package(
        package_name=package_name,
        summary="This is the summary",
        description="Full Description Here",
        home_page="https://www.google.com",
        package_license="MIT",
        author_name="Andy Parinas",
        maintainers=[]
    )

    return package


def get_latest_release_for_package(package_name: str):
    return Release('1.2.0,', datetime.now())
