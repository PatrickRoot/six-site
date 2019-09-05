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
from flask import render_template

from config.config import page_size
from config.db import select_list, select_one


def posts_by_tag(post_type, page_num):
    limit_begin = (page_num - 1) * page_size

    return select_list('''
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

    return select_list('''
select *
from app_posts
where post_status = '1'
order by create_time desc 
limit %d,%d
    ''' % (limit_begin, page_size))


def count_num():
    return select_one('''
select count(1) as count 
from app_posts
where post_status = '1'
    ''')['count']


def count_num_by_type(post_type):
    return select_one('''
select count(1) as count 
from app_posts
where post_status = '1'
and post_type = '%s'
    ''' % post_type)['count']


def render_list(posts_list, url_prefix, page_num, total_number):
    total_page = (total_number + page_size - 1) // page_size

    begin = page_num - 2

    if begin < 1:
        begin = 1

    end = begin + 5

    if end > total_page + 1:
        end = total_page + 1

    return render_template('thoughts/list.html',
                           posts_list=posts_list,
                           url_prefix=url_prefix,
                           page_no=page_num,
                           begin=begin,
                           end=end,
                           total_num=total_number,
                           total_page=total_page)
