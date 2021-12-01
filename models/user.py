from datetime import datetime
import sqlalchemy as sa
from models.model_base import SQLAlchemyBase


class User(SQLAlchemyBase):

    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    email = sa.Column(sa.String, index=True, unique=True)
    hashed_password = sa.Column(sa.String)
    created_at = sa.Column(sa.DateTime, default=datetime.now, index=True)
    profile_image = sa.Column(sa.String, default=datetime.now)
    last_login = sa.Column(sa.DateTime)


