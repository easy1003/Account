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


def query_by_date(args):
    pass

def query_by_category(uid, category, page):
    page = int(page)
    res=[]
    with DbSession() as db_session:

        account_results = db_session.query(AccAccount).join(AccUserAccount,AccAccount.id == AccUserAccount.acc_id).filter(AccUserAccount.uid==uid,AccAccount.category==category).limit(10).offset((page)*10).all()

        if account_results:
            res=trasform_account(account_results)
        left = db_session.query(AccAccount).join(AccUserAccount,AccAccount.id == AccUserAccount.acc_id).filter(AccUserAccount.uid==uid,AccAccount.category==category).limit(10).offset((page+1)*10).all()
        has_next = False
        if left:
            has_next = True

        return {'data': res, 'has_next': has_next, 'page': page}

def query_account(uid,label,category,from_date,to_date,page):
    page = int(page)
    res = []
    filter = []
    filter.append(AccUserAccount.uid==uid)
    if label is not None:
        if int(label) !=3:
            filter.append(AccAccount.label == label)
    if category is not None:
        if int(category)!=0:
            filter.append(AccAccount.category==category)
    if from_date is not None and to_date is not None:
        print(from_date)
        print(to_date)
        filter.append(AccAccount.datetime >= from_date)
        filter.append(AccAccount.datetime <= to_date)
    with DbSession() as db_session:
        account_results = db_session.query(AccAccount).join(AccUserAccount,AccAccount.id == AccUserAccount.acc_id)\
            .filter(*filter).limit(10).offset((page)*10).all()
        if account_results:
            res=trasform_account(account_results)
        left = db_session.query(AccAccount).join(AccUserAccount, AccAccount.id == AccUserAccount.acc_id)\
            .filter(*filter).limit(10).offset((page + 1) * 10).all()
        has_next = False
        if left:
            has_next = True
        return {'data': res, 'has_next': has_next, 'page': page}

def trasform_account(results):
    res=[]
    for result in results:
        event = {}
        event['id'] = result.id
        event['label'] = result.label
        event['category'] = result.category
        event['content'] = result.content
        event['num'] = result.num
        event['money'] = result.money
        event['extra_text'] = result.extra_text
        event['datetime'] = result.datetime.strftime("%Y-%m-%d")
        res.append(event)
    return res