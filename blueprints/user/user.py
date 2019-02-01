#coding:utf-8
import logging
import random

import hashlib
from flask import Blueprint, session, request, render_template

from blueprints.user.services import login_service

from utils.errors.success import succ_json
from utils.errors.parameter_errors import BadRequest
from utils.object_attr_ops import mask_pass


routes = Blueprint('user', __name__, template_folder='templates')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user_id, user_info = login_service.login(username, password)
        return succ_json(mask_pass(user_info))
    else:
        return render_template(
            'login/login.html'
        )

@routes.route('success')
def login_success():
    return render_template('success.html')

@routes.route('index')
def index():
    user={'nickname':'Jack'}
    return render_template(
        "index.html",
        title='Welcome',
        user=user
    )
