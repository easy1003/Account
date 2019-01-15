import logging

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.util import deprecated

from utils.config import get_config
from utils.logger import get_logger

_DATABASE_CONFIG = get_config()['database']

_DB_PARAMS = ['pool_size', 'echo', 'echo_pool', 'max_overflow', 'pool_timeout', 'pool_recycle']


# 检查是否缺少数据库配置参数
for attr in _DB_PARAMS:
    if attr not in _DATABASE_CONFIG:
        raise ValueError("Database configuration field <%s> not found" % attr)

engine = create_engine(_DATABASE_CONFIG['url'],
                       pool_size=_DATABASE_CONFIG['pool_size'],
                       max_overflow=_DATABASE_CONFIG['max_overflow'],
                       echo=_DATABASE_CONFIG['echo'],
                       echo_pool=_DATABASE_CONFIG['echo_pool'],
                       pool_timeout=_DATABASE_CONFIG['pool_timeout'],
                       pool_recycle=_DATABASE_CONFIG['pool_recycle']
                       # pool_pre_ping=True
                       )

_DB_SESSION_FACTORY = sessionmaker(bind=engine)

logger = get_logger()

def on_checkout(dbapi_conn, connection_rec, connection_proxy):
    logger.debug("\ncheckout%s"%dbapi_conn)
    logger.debug("Status: %s\n" % engine.pool.status())


def on_checkin(dbapi_conn, connection_rec):
    logger.debug("\n checkin%s"%dbapi_conn)
    logger.debug("Status: %s\n" % engine.pool.status())


class DbSession:
    def __init__(self):
        self.db_session = _DB_SESSION_FACTORY()

    def __enter__(self):
        return self.db_session

    def __exit__(self, exc_type, exc_val, exc_tb):
        # logger.debug('\nDB Session released...\n')
        self.db_session.close()

    def get_session(self):
        return self.db_session


