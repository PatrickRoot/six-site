"""
Copyright (c) [2019] [sixlab.cn]
[https://github.com/PatrickRoot/six-site] is licensed under the Mulan PSL v1.
You can use this software according to the terms and conditions of the Mulan PSL v1.
You may obtain a copy of Mulan PSL v1 at:
    http://license.coscl.org.cn/MulanPSL
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR
PURPOSE.
See the Mulan PSL v1 for more details.
"""
import datetime
import hashlib

import jwt
from flask import Blueprint, render_template, jsonify, make_response, request, redirect, url_for

from config import utils
from config.db import select_one

app_users = Blueprint('app_users', __name__)


@app_users.route("/info/<username>")
def info(username):
    user = select_one('''
            select * 
            from app_user
            where username = '%s'
        ''' % username)
    return render_template('user/intro.html', user=user)


@app_users.route("/login", methods=['GET'])
def login_get():
    message = request.args.get('message')
    if not message:
        message = ''
    return render_template('user/login.html', message=message)


@app_users.route("/login_json", methods=['POST'])
def login_json():
    result = login()
    resp = jsonify(result)

    if result["success"]:
        resp.set_cookie('token', result['token'], expires=result['expires'])

    return resp


@app_users.route("/login", methods=['POST'])
def login_post():
    result = login()
    resp = redirect(url_for('app_users.login_get', message=result["message"]))

    if result["success"]:
        resp.set_cookie('token', result['data'], expires=result['expires'])

    return resp


def login():
    username = request.form['username']
    password = request.form['password']

    user = select_one('''
            select * 
            from app_user
            where username = '%s'
        ''' % username)

    if not user:
        message = "用户不存在"
    else:
        encrypt = hashlib.md5(hashlib.sha256(password.encode("utf-8")).hexdigest().encode("utf-8")).hexdigest()

        if encrypt == user["password"]:
            date = datetime.datetime.today() + datetime.timedelta(days=1)

            token = jwt.encode({
                "username": username,
                "exp": int(date.timestamp())
            }, 'secret', algorithm='HS256').decode('utf-8')

            return {
                "success": True,
                "data": token,
                "expires": date,
                "message": "登录成功"
            }

        else:
            message = "密码不正确"

    return {
        "success": False,
        "message": message
    }
