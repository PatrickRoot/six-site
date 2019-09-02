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

from flask import Flask, render_template

from apps.posts import app_posts
from apps.tags import app_tags
from apps.thought import app_thought
from apps.types import app_types
from apps.users import app_users
from config.init import init_table

init_table()
app = Flask(__name__)

app.register_blueprint(app_posts, url_prefix='/posts')
app.register_blueprint(app_tags, url_prefix='/tags')
app.register_blueprint(app_types, url_prefix='/types')
app.register_blueprint(app_users, url_prefix='/users')
app.register_blueprint(app_thought, url_prefix='/thought')


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
