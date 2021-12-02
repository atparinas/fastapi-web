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

    session = db_session.create_session()
    try:
        package = session.query(Package).filter(Package.id == package_name).first()
        return package
    finally:
        session.close()


def get_latest_release_for_package(package_name: str):

    session = db_session.create_session()
    try:
        release = session.query(Release).filter(Release.package_id == package_name) \
            .order_by(Release.created_date.desc()) \
            .first()
        return release
    finally:
        session.close()
