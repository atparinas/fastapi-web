from pathlib import Path
from typing import Callable, Optional

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import Session
from models.model_base import SQLAlchemyBase

_factory: Optional[Callable[[], Session]] = None
_async_engine: Optional[AsyncEngine] = None

def global_init(db_file: str):
    global _factory
    global _async_engine

    if _factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Database file must be specified")

    folder = Path(db_file).parent
    folder.mkdir(parents=True, exist_ok=True)

    # con_str = 'sqlite:///' + db_file.strip()
    # print("Connecting to DB with {}".format(con_str))
    conn_str = 'sqlite+pysqlite:///' + db_file.strip()
    async_conn_str = 'sqlite+aiosqlite:///' + db_file.strip()
    print("Connecting to DB with {}".format(async_conn_str))

    engine = sa.create_engine(conn_str, echo=False)
    _async_engine = create_async_engine(async_conn_str, echo=False)
    _factory = orm.sessionmaker(bind=engine)

    import models.__all_models

    SQLAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:

    global _factory

    if not _factory:
        raise Exception("You must call global_init() before calling this method")

    session: Session = _factory()
    session.expire_on_commit = False

    return session


def create_async_session() -> AsyncSession:
    global _async_engine
    if not _async_engine:
        raise Exception("You must call global_init() before calling this method")

    session: AsyncSession = AsyncSession(_async_engine)
    session.sync_session.expire_on_commit = False

    return session


