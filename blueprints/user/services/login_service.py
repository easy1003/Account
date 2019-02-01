from flask import session

from models.ACC_USER import AccUser
from utils.db_connection import DbSession


def login(username, password):
    with DbSession() as db_session:
        register_user = db_session.query(AccUser).filter(AccUser.username==username).first()
        if register_user is None:
            return ;
        else:
            if register_user.password!=password:
                return None
            else:
                userid=register_user.id;
                session['userid']=userid
                session['username']=username
                return  userid,register_user._as_dict()









