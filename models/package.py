from datetime import datetime
from typing import List
import sqlalchemy as sa
from sqlalchemy import orm

from models.model_base import SQLAlchemyBase
from models.release import Release


class Package(SQLAlchemyBase):
    __tablename__ = 'packages'

    id: str = sa.Column(sa.String, primary_key=True)
    created_date: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    last_updated: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    summary: str = sa.Column(sa.String, nullable=False)
    description: str = sa.Column(sa.String, nullable=True)

    home_page: str = sa.Column(sa.String)
    docs_url: str = sa.Column(sa.String)
    package_url: str = sa.Column(sa.String)

    author_name: str = sa.Column(sa.String)
    author_email: str = sa.Column(sa.String, index=True)

    license: str = sa.Column(sa.String, index=True)

    # releases relationship
    releases: List[Release] = orm.relationship("Release", order_by=[
        Release.major_ver.desc(),
        Release.minor_ver.desc(),
        Release.build_ver.desc(),
    ], back_populates='package')

    def __repr__(self):
        return '<Package {}>'.format(self.id)

