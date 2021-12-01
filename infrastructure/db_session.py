from pathlib import Path
from typing import Callable, Optional

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
from models.model_base import SQLAlchemyBase

_factory: Optional[Callable[[], Session]] = None


def global_init(db_file: str):
    global _factory

    if _factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Database file must be specified")

    folder = Path(db_file).parent
    folder.mkdir(parents=True, exist_ok=True)

    con_str = 'sqlite:///' + db_file.strip()
    print("Connecting to DB with {}".format(con_str))

    engine = sa.create_engine(con_str, echo=False)
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

