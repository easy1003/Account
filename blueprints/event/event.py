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


@routes.route('/query_index',methods=['GET'])
@require_login
def query_index():
    if request.method == 'GET':
        pass
    else :
        pass

