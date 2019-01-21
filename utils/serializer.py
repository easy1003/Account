import json

from flask import Response
from sqlalchemy.ext.declarative import DeclarativeMeta


class FlatObjectEncoder(json.JSONEncoder):
    """Simple, non-recursive json encoder"""

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata' and not x.startswith('rl_')]:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


def obj_to_json(obj):
    """Simply convert flat SQLAlchemy objects into json"""
    return json.dumps(obj, cls=FlatObjectEncoder)
