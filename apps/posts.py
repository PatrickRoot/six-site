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

from config.db import run_sql2, select_one
from config.utils import login_user

app_posts = Blueprint('app_posts', __name__)


@app_posts.route("/auth/add")
def add():
    return render_template('posts/add.html', id="")


@app_posts.route("/auth/edit/<int:post_id>")
def edit(post_id):
    return render_template('posts/add.html', id=post_id)


@app_posts.route("/auth/post/<int:post_id>", methods=['POST'])
def post(post_id):
    app_posts = select_one('''
    select *
    from app_posts
    where id = %d
    ''' % (post_id,))

    app_tags = select_one('''
    select group_concat(at.tag_name) as tags
    from app_tags at,app_posts_tags apt 
    where at.id = apt.tag_id
    and apt.post_id = %d
    '''%(post_id,))

    if app_tags:
        app_tags = app_tags['tags']

    return jsonify({
        "success": True,
        "data":{
            "post": app_posts,
            "tags": app_tags,
        }
    })


@app_posts.route("/auth/submit", methods=['POST'])
def submit():
    id = request.form.get("id")
    title = request.form.get("title")
    markdwon = request.form.get("markdwon")
    content = request.form.get("content")
    summary = request.form.get("summary")
    type = request.form.get("type")
    date = request.form.get("date")
    username = login_user()

    if len(summary) > 200:
        summary = summary[:200]

    if not id:
        run_sql2('''
        INSERT INTO app_posts 
        (post_type, post_title, post_summary, post_content, post_content_origin, post_status, view_count, thumb_count, comment_count, create_user, create_time) 
        VALUES 
        (?, ?, ?, ?, ?, '1', 0, 0, 0, ?, ?)
        ''', (type, title, summary, content, markdwon, username, date))
    else:
        run_sql2('''
        UPDATE app_posts 
        SET 
        post_type = ?, 
        post_title = ?, 
        post_summary = ?, 
        post_content = ?, 
        post_content_origin = ?, 
        post_status = '1', 
        view_count = 0, 
        thumb_count = 0, 
        comment_count = 0, 
        create_user = ?, 
        create_time = ? 
        WHERE id = ?
        ''', (type, title, summary, content, markdwon, username, date, id))

        run_sql2('''
        DELETE FROM app_posts_tags 
        WHERE post_id = ?
        ''', (id,))

        tags = request.form.get("tags")

        if len(tags) > 0:
            tag_names = tags.split(",")

            for tag_name in tag_names:
                app_tags = select_one('''
                select *
                from app_tags
                where tag_name = '%s'
                ''' % tag_name)

                if not app_tags:
                    run_sql2('''
                    INSERT INTO app_tags 
                    (tag_name) 
                    VALUES 
                    (?);
                    ''', (tag_name,))

                    app_tags = select_one('''
                                select *
                                from app_tags
                                where tag_name = '%s'
                                ''' % tag_name)

                run_sql2('''
                INSERT INTO app_posts_tags
                (post_id, tag_id) 
                VALUES 
                (?, ?)
                ''', (id, app_tags["id"]))

    return jsonify({
        "success": True
    })
