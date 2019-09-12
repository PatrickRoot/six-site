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

from flask import Blueprint, render_template, jsonify, request
from datetime import datetime

from config import utils
from config.db import select_list, run_sql, select_one

app_comments = Blueprint('app_comments', __name__)


@app_comments.route("/list/<int:post_id>", methods=['GET', 'POST'])
def list(post_id):

    app_comments = select_list('''
    select *
    from app_comment
    where post_id = ?
    order by id desc 
    ''', (post_id,))

    username = utils.login_user()

    if not username:
        username = ''

    return render_template('comments/list.html', post_id=post_id, app_comments=app_comments, username=username)


@app_comments.route("/thumb", methods=['POST'])
def thumb():
    comment_id = request.form["commentId"]
    run_sql('''
    update app_comment
    set thumb_count = thumb_count + 1
    where id = ?
    ''', (comment_id,))

    app_posts = select_one('''
                select * 
                from app_comment 
                where id = ?
            ''', (comment_id,))

    return jsonify({
        "success": True,
        "data": app_posts['thumb_count']
    })


@app_comments.route("/submit/<int:post_id>", methods=['POST'])
def submit(post_id):
    username = request.form['username']
    comment_content = request.form['commentContent']
    reply_id = request.form['replyId']

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    run_sql('''
    INSERT INTO app_comment (post_id, reply_id, reply_count, thumb_count, comment_content, create_user, create_time) 
    VALUES (?, ?, 0, 0, ?, ?, ?);
    ''', (post_id, reply_id, comment_content, username, now))

    run_sql('''
    update app_posts
    set comment_count = comment_count + 1
    where id = ?
    ''', (post_id,))

    return jsonify({
        "success": True,
        "data": now,
    })


@app_comments.route("/auth/post/<int:post_id>", methods=['POST'])
def post(post_id):
    return jsonify({
        "success": True,
    })
