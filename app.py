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
from config.db import run_sql
from config.init import init_table
from models.posts import posts_by_num, count_num, render_list

init_table()
app = Flask(__name__)

app.register_blueprint(app_posts, url_prefix='/posts')
app.register_blueprint(app_tags, url_prefix='/tags')
app.register_blueprint(app_thought, url_prefix='/thought')
app.register_blueprint(app_thoughts, url_prefix='/thoughts')
app.register_blueprint(app_users, url_prefix='/users')


@app.route('/')
def index():
    posts_list = posts_by_num(1)
    total_number = count_num()
    return render_list(posts_list=posts_list, url_prefix=url_for("app_thoughts.index")+"p/", page_num=1, total_number=total_number)


@app.route("/init")
def init():

    run_sql('''
update app_posts set post_type = 'blog' where post_type = '0'
    ''')

    run_sql('''
update app_posts set post_type = 'forum' where post_type = '1'
    ''')
    run_sql('''
update app_posts set post_type = 'mine' where post_type = '2'
    ''')

    return """
    INSERT INTO app_posts 
    (post_type, post_title, post_content, post_status, view_count, thumb_count, comment_count, create_user, create_time, post_content_origin)
     VALUES 
    ('blog', 'b1', 'c1', '1', 0, 0, 0, 'user', '', null)
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
