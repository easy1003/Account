import datetime

from sqlalchemy import String, Integer, Column, Text, Date
from sqlalchemy.orm import relationship

from models.BASE import BASE
from utils.db_connection import DbSession
from sqlalchemy.sql import func


class AccUser (BASE):
    __tablename__ = "ACC_USER"
    id = Column('ID', Integer, primary_key=True)
    username = Column('USERNAME', String(32))
    password = Column('PASSWORD', String(32))
    realname = Column('REALNAME', String(32))
    nickname = Column('NICKNAME', String(32))
    avatar = Column('AVATAR', String(20))
    signature = Column('SIGNATURE', Text)
    wx_id = Column('WX_ID', String(30))
    sex = Column('SEX', Integer, default=0)
    birthday = Column('BIRTHDAY', Date, default=datetime.date(2016, 10, 10))
    mobile = Column('MOBILE', String(15))
    status = Column('STATUS', Integer, default=1)

    def __init__(self, username, password, **kwargs):
        self.username = username
        self.password = password
        self.realname = kwargs.get('realname')
        self.nickname = kwargs.get('nickname')
        self.avatar = kwargs.get('avatar')
        self.signature = kwargs.get('signature')
        self.sex = kwargs.get('sex')
        self.wx_id = kwargs.get('wx_id')
        self.birthday = kwargs.get('birthday')
        self.mobile = kwargs.get('mobile')
        self.status = kwargs.get('status')

    def _as_dict(self):
        res = {}
        for attr in ['id', 'username', 'password', 'realname', 'nickname', 'avatar', 'signature', 'wx_id', 'sex',
                     'mobile', 'status']:
            res[attr] = getattr(self, attr)
        res['birthday'] = str(self.birthday)
        return res

if __name__ == '__main__':
    with DbSession() as db_session:
        user = db_session.query(AccUser).one()
        print(user._as_dict())