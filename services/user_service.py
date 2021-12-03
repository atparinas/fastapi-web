from typing import Optional

from sqlalchemy import func
from sqlalchemy.engine import Result
from sqlalchemy.future import select

from infrastructure import db_session
from models.user import User
from passlib.handlers.sha2_crypt import sha512_crypt as crypto


async def user_count() -> int:
    async with db_session.create_async_session() as session:
        query = select(func.count(User.id))

        result = await session.execute(query)

        return result.scalar()

    # session = db_session.create_session()
    #
    # try:
    #     return session.query(User).count()
    # finally:
    #     session.close()


async def create_account(name: str, email: str, password: str):
    custom_crypt = crypto.using(rounds=214214)
    user = User()
    user.email = email
    user.name = name
    user.hashed_password = custom_crypt.hash(password)

    async with db_session.create_async_session() as session:
        session.add(user)
        await session.commit()

    return user


    # session = db_session.create_session()
    #
    # custom_crypt = crypto.using(rounds=214214)
    #
    # try:
    #     user = User()
    #     user.email = email
    #     user.name = name
    #     user.hashed_password = custom_crypt.hash(password)
    #
    #     session.add(user)
    #     session.commit()
    #
    #     return user
    # finally:
    #     session.close()


async def login_user(email: str, password: str):

    async with db_session.create_async_session() as session:
        query = select(User).filter(User.email == email)
        result = await session.execute(query)

        user = result.scalar_one_or_none()

        if not user:
            return None

        if not crypto.verify(secret=password, hash=user.hashed_password):
            return None

        return user


    # session = db_session.create_session()
    # try:
    #     user = session.query(User).filter(User.email == email).first()
    #     if not user:
    #         return None
    #     if not crypto.verify(secret=password, hash=user.hashed_password):
    #         return None
    #
    #     return user
    #
    # finally:
    #     session.close()


async def get_user_by_id(id: int) -> Optional[User]:
    async with db_session.create_async_session() as session:
        query = select(User).filter(User.id == id)

        result: Result = await session.execute(query)

        return result.scalar_one_or_none()

    # session = db_session.create_session()
    # try:
    #     user = session.query(User).filter(User.id == id).first()
    #     return user
    # finally:
    #     session.close()
