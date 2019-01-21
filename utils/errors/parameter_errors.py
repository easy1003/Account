from utils.errors.base_error import BaseError


class BadRequest(BaseError):
    status_code = 200

    def __init__(self, code, msg, status_code=None, payload=None):
        Exception.__init__(self)
        self.code = code
        self.msg = msg
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = {'code': self.code, 'msg': self.msg}
        if self.payload is not None:
            rv['data'] = self.payload
        return rv


class UnauthorizedError(BaseError):
    status_code = 200

    def __init__(self, code, msg, status_code=None, payload=None):
        Exception.__init__(self)
        self.code = code
        self.msg = msg
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = {'code': self.code, 'msg': self.msg}
        if self.payload is not None:
            rv['data'] = self.payload
        return rv