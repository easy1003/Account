import datetime

from sqlalchemy import String, Integer, Column, Text, Date
from sqlalchemy.orm import relationship

from models.BASE import BASE


class AccUserAccount(BASE):
    __tablename__= 'ACC_USER_ACCOUNT'
    id = Column('ID', Integer, primary_key=True, autoincrement='ignore_fk')
    uid = Column('UID', String(32))
    acc_id = Column('ACC_ID', Integer)
    status = Column('STATUS', Integer, default=1)

    def __init__(self, **kwargs):
        self.uid = kwargs.get('uid')
        self.acc_id = kwargs.get('acc_id')

    def __repr__(self):
        return 'ACC_USER_ACCOUNT %s'.format(self.id)

    def _as_dict(self):
        res = {}
        for attr in ['id','uid', 'acc_id', 'status']:
            res[attr]=getattr(self,attr)
        return res