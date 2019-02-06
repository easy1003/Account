from datetime import datetime

from flask import session

from models.ACC_CATEGORY import AccCategory
from models.ACC_ACCOUNT import AccAccount
from models.ACC_USER_ACCOUNT import AccUserAccount
from models.ACC_MONEY import AccMoney
from utils.db_connection import DbSession
from utils.errors.parameter_errors import BadRequest




def add_account(args):
    uid=session.get('userid')
    label=args.get('label')
    category=args.get('category')
    money=args.get('money')
    content=args.get('content')
    num=args.get('num')
    extra_text=args.get('extra_text')
    date=args.get('datetime')


    categorys=get_catrgory()
    print("*"*15)
    print(args)
    print(label)
    print(categorys[int(category)-1])
    print(type(label))
    print("*" * 15)
    if int(label) != categorys[int(category)-1].get('status'):
        return False, '参数错误'

    acc_account= AccAccount(
        label=int(label),category=int(category),money=int(money),
        content=content,num=int(num),extra_text=extra_text,
        datetime=date
    )
    print(acc_account._as_dict())
    print(acc_account.datetime)
    with DbSession() as db_session:
        result=db_session.add(acc_account)
        db_session.commit()
        print(acc_account.id)
        acc_user_account = AccUserAccount(
            uid=uid, acc_id=acc_account.id
        )
        db_session.add(acc_user_account)
        db_session.commit()

    return True, None

def get_catrgory():
    """
    获取消费类别
    :return:
    """
    with DbSession() as db_session:
        categorys = db_session.query(AccCategory).all()
        result=[]
        for category in categorys:
            result.append(category._as_dict())

        return result


def query_by_date():
    pass
