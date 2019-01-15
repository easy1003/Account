# encoding:utf-8
import logging

_log_file = 'logs/all.log'
_flask_log = 'logs/flask.log'

_logger = logging.getLogger('sjd')
_logger.setLevel(logging.DEBUG)

_file_handler = logging.FileHandler(_log_file)
_file_handler.setLevel(logging.DEBUG)

_console_handler = logging.StreamHandler()
_console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("""
----%(asctime)s - %(name)s - %(levelname)s ----
%(message)s
""")
_file_handler.setFormatter(formatter)
_console_handler.setFormatter(formatter)

# add handlers to logger
_logger.addHandler(_file_handler)
_logger.addHandler(_console_handler)

# SQLAlchemy logging config
# see: http://docs.sqlalchemy.org/en/latest/core/engines.html#dbengine-logging

# logging.getLogger('sqlalchemy.engine').addHandler(_file_handler)
# logging.getLogger('sqlalchemy.engine').addHandler(_console_handler)

# flask logging config
_flask_log_handler = logging.FileHandler(_flask_log)
_flask_log_handler.setLevel(logging.DEBUG)

# access logging config
_access_log_handler = logging.FileHandler('logs/access.log')
_werkzeug_logger = logging.getLogger('werkzeug')
_werkzeug_logger.addHandler(_access_log_handler)


def get_flask_log_handler():
    return _flask_log_handler


def get_logger():
    return _logger


if __name__ == '__main__':
    try:
        raise TypeError('oops')
    except TypeError as e:
        # stack_info=True 输出所有的调用栈
        get_logger().warning(e, stack_info=True)

