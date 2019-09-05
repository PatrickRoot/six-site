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

from flask import Blueprint, url_for

from config.config import page_size
from config.db import select_list, select_one
from models.posts import render_list

app_tags = Blueprint('app_tags', __name__)


# 标签
@app_tags.route("/<tag_code>/")
def tags(tag_code):
    posts_list = posts_by_tag(tag_code, 1)
    total_number = count_num_by_tag(tag_code)
    return render_list(posts_list=posts_list, url_prefix=url_for("app_tags.tags", tag_code=tag_code), page_num=1,
                       total_number=total_number)


# 标签
@app_tags.route("/<tag_code>/<int:page_num>")
def tags_page(tag_code, page_num):
    posts_list = posts_by_tag(tag_code, page_num)
    total_number = count_num_by_tag(tag_code)
    return render_list(posts_list=posts_list, url_prefix=url_for("app_tags.tags", tag_code=tag_code), page_num=page_num,
                       total_number=total_number)


def count_num_by_tag(tag_code):
    return select_one('''
            select count(1) as count
            from app_posts ap
            where ap.post_status = '1'
              and exists(
                    select 1
                    from app_posts_tags apt
                    where apt.post_id = ap.id
                      and apt.tag_code = '%s'
                )
        ''' % tag_code)['count']


def posts_by_tag(tag_name, page_num):
    limit_begin = (page_num - 1) * page_size

    return select_list('''
            select ap.*
            from app_posts ap
            where ap.post_status = '1'
              and exists(
                    select 1
                    from app_posts_tags apt
                    where apt.post_id = ap.id
                      and apt.tag_code = '%s'
                )
            order by ap.create_time desc 
            limit %d,%d
        ''' % (tag_name, limit_begin, page_size))
