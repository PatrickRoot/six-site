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

from flask import Flask, url_for

from apps.posts import app_posts
from apps.tags import app_tags
from apps.thought import app_thought
from apps.thoughts import app_thoughts
from apps.users import app_users
from config.filter import menu_tags
from config.init import init_table
from models.posts import posts_by_num, count_num, render_list

init_table()
app = Flask(__name__)

env = app.jinja_env
# env.filters['menu_tags'] = menu_tags
env.globals["menu_tags"] = menu_tags

app.register_blueprint(app_posts, url_prefix='/posts')
app.register_blueprint(app_tags, url_prefix='/tags')
app.register_blueprint(app_thought, url_prefix='/thought')
app.register_blueprint(app_thoughts, url_prefix='/thoughts')
app.register_blueprint(app_users, url_prefix='/user')


@app.route('/')
def index():
    posts_list = posts_by_num(1)
    total_number = count_num()
    return render_list(posts_list=posts_list, url_prefix=url_for("app_thoughts.index")+"p/", page_num=1, total_number=total_number)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
