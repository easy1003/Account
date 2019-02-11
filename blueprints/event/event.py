#coding:utf-8
import logging
import random
import os
import hashlib
from flask import Blueprint, session, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from blueprints.event.services import event_service

from utils.errors.success import succ_json
from utils.errors.parameter_errors import BadRequest
from utils.object_attr_ops import mask_pass
from utils.require_login import require_login

routes = Blueprint('event', __name__, static_folder='static', template_folder='templates')

@routes.route('/index',methods=['GET','POST'])
@require_login
def index():

    return render_template(
        'event_index.html'
    )

@routes.route('/add_event',methods=['GET','POST'])
@require_login
def add_event():

    if request.method == 'POST':
        res, msg = event_service.add_account(request.form.to_dict())
        if not res:
            return BadRequest('1', msg)
        return succ_json(msg)

    else:
        categorys = event_service.get_catrgory()

        return render_template(
            'add_event.html', categorys=categorys
        )

@routes.route('/query_event',methods=['GET'])
@require_login
def query_event():
    if request.method == 'GET':

        pass
    else:
        pass


@routes.route('/query_index',methods=['GET','POST'])
@require_login
def query_index():
    categorys = event_service.get_catrgory()
    if request.method == 'POST':
        label = request.form.get('label')
        category = request.form.get('category')
        page = request.form.get('page')
        from_date = request.form.get('from_date')
        to_date = request.form.get('to_date')
        if not page:
            page = 0
        uid = session.get('userid')
        res = event_service.query_account(uid=uid,label=label,category=category
                                          ,from_date=from_date,to_date=to_date,page=page)

        # if category is not None:
        #     res = event_service.query_by_category(uid=uid, category=category, page=page)
        #     accounts=res['data']
        #     return render_template(
        #         'query_event.html',accounts=accounts,categorys=categorys
        #     )
        return succ_json(res)
    else :
        return render_template(
            'query_index.html', categorys=categorys
        )



