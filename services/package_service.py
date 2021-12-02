from datetime import datetime
from typing import List, Optional

from sqlalchemy import orm

from models.package import Package
from models.release import Release

from infrastructure import db_session


def release_count():
    session = db_session.create_session()

    try:
        return session.query(Release).count()
    finally:
        session.close()


def package_count():
    session = db_session.create_session()

    try:
        return session.query(Package).count()
    finally:
        session.close()


def latest_releases(limit: int = 10) -> List[Package]:
    session = db_session.create_session()

    try:
        releases = session.query(Release) \
            .options(orm.joinedload(Release.package)) \
            .order_by(Release.created_date.desc()) \
            .limit(limit) \
            .all()
    finally:
        session.close()

    return list({r.package for r in releases})


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
