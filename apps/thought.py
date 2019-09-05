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

from flask import Blueprint, render_template, redirect, url_for

from config.db import select_one, select_list

app_thought = Blueprint('app_thought', __name__)


@app_thought.route("/")
def thought_index():
    return redirect(url_for('app_thoughts.index'))


@app_thought.route("/<int:id>")
def thought(id):
    app_posts = select_one('''
    select * from app_posts where id = %d
    ''' % id)

    app_tags = select_list('''
select *
from app_tags at
where exists(
              select 1
              from app_posts_tags apt
              where apt.tag_code = at.tag_code
                and apt.post_id = %d
          )
    ''' % app_posts['id'])

    return render_template('thoughts/thought.html', app_posts=app_posts, app_tags=app_tags)
