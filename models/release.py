import datetime

import sqlalchemy as sa
from sqlalchemy import orm

from models.model_base import SQLAlchemyBase


class Release(SQLAlchemyBase):

    __tablename__ = 'releases'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    major_ver: int = sa.Column(sa.BigInteger, index=True)
    minor_ver: int = sa.Column(sa.BigInteger, index=True)
    build_ver: int = sa.Column(sa.BigInteger, index=True)

    created_date: datetime.datetime = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)

    comment: str = sa.Column(sa.String)
    url: str = sa.Column(sa.String)
    size: int = sa.Column(sa.BigInteger)

    package_id: str = sa.Column(sa.String, sa.ForeignKey("packages.id"))
    package = orm.relation('Package')

    @property
    def version_text(self):
        return "{}:{}:{}".format(self.major_ver, self.major_ver, self.build_ver)