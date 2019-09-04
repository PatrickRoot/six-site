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

from flask import Blueprint, render_template, url_for

from models.posts import posts_by_num, count_num, posts_by_tag, count_num_by_type, render_list

app_thoughts = Blueprint('app_thoughts', __name__)


# 标签
@app_thoughts.route("/")
def index():
    posts_list = posts_by_num(1)
    total_number = count_num()
    return render_list(posts_list=posts_list, url_prefix=url_for("app_thoughts.index") + "p/", page_num=1, total_number=total_number)


@app_thoughts.route("/p/<int:page_num>")
def index_list(page_num):
    posts_list = posts_by_num(page_num)
    total_number = count_num()
    return render_list(posts_list=posts_list, url_prefix=url_for("app_thoughts.index") + "p/", page_num=page_num, total_number=total_number)


# 标签
@app_thoughts.route("/t/<string:post_type>/")
def thoughts_list(post_type):
    posts_list = posts_by_tag(post_type, 1)
    total_number = count_num_by_type(post_type)
    return render_list(posts_list=posts_list, url_prefix=url_for("app_thoughts.thoughts_list", post_type=post_type), page_num=1, total_number=total_number)


@app_thoughts.route("/t/<string:post_type>/<int:page_num>")
def thoughts_lists(post_type, page_num):
    posts_list = posts_by_tag(post_type, page_num)
    total_number = count_num_by_type(post_type)
    return render_list(posts_list=posts_list, url_prefix=url_for("app_thoughts.thoughts_list", post_type=post_type), page_num=page_num, total_number=total_number)
