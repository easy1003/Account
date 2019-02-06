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
    id = Column('ID', Integer, primary_key=True, autoincrement='ignore_fk')
    label = Column('LABEL', Integer, default=1)
    category = Column('CATEGORY', Integer, ForeignKey(AccCategory.id))
    content = Column('CONTENT', String(100))
    num = Column('NUM',Integer)
    money = Column('MONEY', Integer, ForeignKey(AccMoney.id))
    extra_text = Column('EXTRA_TEXT', String(200))
    datetime = Column('DATETIME',Date,default=datetime.date(2019, 1, 1) )

    def __init__(self, **kwargs):
        self.label = kwargs.get('label')
        self.category = kwargs.get('category')
        self.content= kwargs.get('content')
        self.num=kwargs.get('num')
        self.money=kwargs.get('money')
        self.extra_text=kwargs.get('extra_text')
        self.datetime=kwargs.get('datetime')

    def __repr__(self):
        return 'ACC_CATEGORY %s'.format(self.id)

    def _as_dict(self):
        res = {}
        for attr in ['id', 'label', 'category','content','num','money','extra_text','datetime']:
            res[attr] = getattr(self, attr)
        return res
