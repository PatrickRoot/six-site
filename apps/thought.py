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

from config.db import run_select_one

app_thought = Blueprint('app_thought', __name__)


@app_thought.route("/")
def thought_index():
    return redirect(url_for('app_thoughts.index'))


@app_thought.route("/<int:id>")
def thought(id):
    app_posts = run_select_one('''
    select * from app_posts where id = %d
    ''' % id)
    return render_template('thoughts/thought.html', app_posts=app_posts)
