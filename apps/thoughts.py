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

from flask import Blueprint, render_template

from config.config import page_size
from config.db import run_select

app_thoughts = Blueprint('app_thoughts', __name__)


# 标签
@app_thoughts.route("/")
def index():
    posts_list = posts_by_num(1)
    return render_template('thoughts/list.html', posts_list=posts_list)


# 标签
@app_thoughts.route("/<string:post_type>/")
def thoughts_list(post_type):
    posts_list = posts_by_tag(post_type, 1)
    return render_template('thoughts/list.html', posts_list=posts_list)


@app_thoughts.route("/<string:post_type>/<int:page_num>")
def thoughts_lists(post_type, page_num):
    posts_list = posts_by_tag(post_type, page_num)
    return render_template('thoughts/list.html', posts_list=posts_list)


def posts_by_tag(post_type, page_num):
    limit_begin = (page_num - 1) * page_size

    return run_select('''
select *
from app_posts
where post_status = '1'
and post_type = '%s'
order by create_time desc 
limit %d,%d
    ''' % (post_type, limit_begin, page_size))


# 查询
def posts_by_num(page_num):
    limit_begin = (page_num - 1) * page_size

    return run_select('''
select *
from app_posts
where post_status = '1'
order by create_time desc 
limit %d,%d
    ''' % (limit_begin, page_size))
