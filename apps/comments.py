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

from flask import Blueprint, render_template, request, jsonify

from config.db import select_list

app_comments = Blueprint('app_comments', __name__)


@app_comments.route("/list/<int:post_id>", methods=['GET', 'POST'])
def list(post_id):

    app_comments = select_list('''
    select *
    from app_comment
    where post_id = ?
    order by id desc 
    ''', (post_id,))

    return render_template('comments/list.html', app_comments=app_comments)


@app_comments.route("/auth/edit/<int:post_id>")
def edit(post_id):
    return render_template('posts/add.html', id=post_id)


@app_comments.route("/auth/post/<int:post_id>", methods=['POST'])
def post(post_id):
    return jsonify({
        "success": True,
    })


@app_comments.route("/auth/submit", methods=['POST'])
def submit():

    return jsonify({
        "success": True
    })
