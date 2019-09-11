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

from flask import Blueprint, render_template, redirect, url_for, jsonify

from config.db import select_one, select_list, run_sql
from config.utils import is_login

app_thought = Blueprint('app_thought', __name__)


@app_thought.route("/")
def thought_index():
    return redirect(url_for('app_thoughts.index'))


@app_thought.route("/<int:id>")
def thought(id):
    run_sql('''
    update app_posts
    set view_count = view_count + 1
    where id = ?
    ''', (id,))

    app_posts = select_one('''
                select * 
                from app_posts 
                where id = ?
            ''', (id,))

    app_tags = select_list('''
            select *
            from app_tags at
            where exists(
                      select 1
                      from app_posts_tags apt
                      where apt.tag_id = at.id
                        and apt.post_id = ?
                  )
        ''', (app_posts['id'],))

    return render_template('thoughts/thought.html', app_posts=app_posts, app_tags=app_tags, is_login=is_login())


@app_thought.route("/thumb/<int:post_id>", methods=['POST'])
def thumb(post_id):
    run_sql('''
    update app_posts
    set thumb_count = thumb_count + 1
    where id = ?
    ''', (post_id,))

    app_posts = select_one('''
                select * 
                from app_posts 
                where id = ?
            ''', (post_id,))

    return jsonify({
        "success":True,
        "data": app_posts['thumb_count']
    })
