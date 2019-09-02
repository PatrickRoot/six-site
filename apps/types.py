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

app_types = Blueprint('app_types', __name__)

# 分类
@app_types.route("/<type_name>")
def types(type_name):
    posts_list = posts_by_type(type_name, 1)
    return render_template('posts/list.html', posts_list=posts_list)


@app_types.route("/<type_name>/<int:page_num>")
def types_page(type_name, page_num):
    posts_list = posts_by_type(type_name, page_num)
    return render_template('posts/list.html', posts_list=posts_list)


def posts_by_type(type_name, page_num):
    limit_begin = (page_num - 1) * page_size

    return run_select('''
select *
from app_posts
where post_status = '1'
and post_type = '%s'
order by create_time desc 
limit %d,%d
    ''' % (type_name, limit_begin, page_size))


if __name__ == '__main__':
    print(posts_by_type("blog",1))
