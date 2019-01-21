#coding:utf-8
import logging
import random

import hashlib
from flask import Blueprint, session, request, render_template
from sqlalchemy.orm.exc import NoResultFound


routes = Blueprint('user', __name__, template_folder='templates')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

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
