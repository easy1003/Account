import datetime

from sqlalchemy import String, Integer, Column, Text, Date
from sqlalchemy.orm import relationship

from models.BASE import BASE
from utils.db_connection import DbSession
from sqlalchemy.sql import func


class AccMoney(BASE):
    __tablename__ = 'ACC_MONEY'
    id = Column('ID', Integer, primary_key=True, autoincrement='ignore_fk' )
    money = Column('MONEY', String(32))
    status = Column('STATUS', Integer, default=1)

    def __init__(self, **kwargs):
        self.category = kwargs.get('money')
        self.status = kwargs.get('status')

    def __repr__(self):
        return 'ACC_CATEGORY %s'.format(self.id)

    def _as_dict(self):
        res = {}
        for attr in ['id', 'money', 'status']:
            res[attr] = getattr(self, attr)
        return res
