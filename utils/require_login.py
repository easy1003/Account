from flask import session
from functools import wraps

from utils.errors.parameter_errors import UnauthorizedError



def require_login(func):
    """

    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('username'):
            return func(*args, **kwargs)
        else:
            raise UnauthorizedError(code=-1, msg='必须先登录')
    return wrapper