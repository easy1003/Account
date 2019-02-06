#coding:utf-8
import logging
import random
import os
import hashlib
from flask import Blueprint, session, request, render_template, redirect, url_for,abort
from werkzeug.utils import secure_filename
from blueprints.user.services import login_service

from utils.errors.success import succ_json
from utils.errors.parameter_errors import BadRequest
from utils.object_attr_ops import mask_pass


routes = Blueprint('user', __name__, static_folder='static', template_folder='templates')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user_id, user_info = login_service.login(username, password)

        return redirect(url_for('event.index'))
    else:
        return render_template(
            'login.html'
        )

@routes.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('user.login'))

@routes.route('success')
def login_success():
    return render_template('/success/success.html')


@routes.route('test')
def test():
    abort(404)


@routes.route('index')
def index():
    user={'nickname':'Jack'}
    return render_template(
        "index.html",
        title='Welcome',
        user=user
    )

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@routes.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('/home/yyz/PycharmProjects/AccountApp/upload', filename))
            return redirect(url_for('user.upload_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

