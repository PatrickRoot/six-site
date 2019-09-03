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

from config.db import run_sql


def init_table():
    # app_config
    run_sql('''
CREATE TABLE IF NOT EXISTS site_config
(
    id INTEGER primary key autoincrement,
    config_key TEXT,
    config_val TEXT,
    create_user TEXT,
    create_time TEXT
);
    ''')

    run_sql('''
CREATE index IF NOT EXISTS site_config_index_config_key on site_config (config_key);
    ''')

    # app_config
    run_sql('''
CREATE TABLE IF NOT EXISTS app_posts
(
    id INTEGER primary key autoincrement,
    post_type TEXT,
    post_title TEXT,
    post_summary TEXT,
    post_content TEXT,
    post_content_origin TEXT,
    post_status TEXT,
    view_count INTEGER,
    thumb_count INTEGER,
    comment_count INTEGER,
    create_user TEXT,
    create_time TEXT
);
    ''')

    run_sql('''
CREATE index IF NOT EXISTS app_posts_index_post_type on app_posts (post_type);
    ''')

    run_sql('''
CREATE index IF NOT EXISTS app_posts_index_post_status on app_posts (post_status);
    ''')
