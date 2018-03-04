from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from .config import Config as conf

db = None

_ENGINE=None

@contextmanager
def db_session(db_url=conf.DATABASE_URI, autoflush=True):
    global _ENGINE
    """ Creates a context with an open SQLAlchemy session.
    """
    if not _ENGINE:
        _ENGINE=create_engine(db_url, convert_unicode=True, pool_size=4)
        
    connection = _ENGINE.connect()
    Session = scoped_session(sessionmaker(autocommit=False, autoflush=autoflush, bind=_ENGINE))
    session = Session()
    yield session
    session.close()
    connection.close()

def get_session(db_url=conf.DATABASE_URI, engine=None):
    """
        Return a session, but need to remember to close
    """
    if not engine:
        engine = create_engine(db_url, convert_unicode=True, pool_size=1)

    connection = engine.connect()
    Session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=engine))
    return Session()


def cleanse(metadata, db_url=conf.DATABASE_URI, autoflush=True):

    with db_session(db_url, autoflush) as sess:
        con = sess.connection()
        for table in reversed(metadata.sorted_tables):
            con.execute(table.delete())
        sess.commit()
