import datetime

from sqlalchemy import String, Integer, Column, Text, Date, ForeignKey
from sqlalchemy.orm import relationship

from models.BASE import BASE
from models.ACC_CATEGORY import AccCategory
from models.ACC_MONEY import AccMoney
from utils.db_connection import DbSession
from sqlalchemy.sql import func


class AccAccount(BASE):
    __tablename__ = 'ACC_ACCOUNT'
    id = Column('ID', Integer, primary_key=True)
    label = Column('LABEL', Integer, default=1)
    category = Column('CATEGORY', Integer, ForeignKey(AccCategory.id))
    content = Column('CONTENT', String(100))
    num = Column('NUM',Integer)
    money = Column('MONEY', Integer, ForeignKey(AccMoney.id))
    extra_text = Column('EXTRA_TEXT', String(200))
    datetime = Column('DATATIME',Integer, default=datetime.time())

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.category = kwargs.get('category')
        self.status = kwargs.get('status')

    def __repr__(self):
        return 'ACC_CATEGORY %s'.format(self.id)

    def _as_dict(self):
        res = {}
        for attr in ['id', 'category', 'status']:
            res[attr] = getattr(self, attr)
        return res
