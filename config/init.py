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
    # 创建 site_config
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

    # site_config 索引
    run_sql('''
CREATE index IF NOT EXISTS site_config_index_config_key on site_config (config_key);
    ''')

    # 创建 app_posts
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

    # app_posts 索引
    run_sql('''
CREATE index IF NOT EXISTS app_posts_index_post_type on app_posts (post_type);
    ''')

    run_sql('''
CREATE index IF NOT EXISTS app_posts_index_post_status on app_posts (post_status);
    ''')

    # 创建 app_tags
    run_sql('''
    CREATE TABLE IF NOT EXISTS app_tags
(
    id INTEGER primary key autoincrement,
    tag_name TEXT,
    tag_code TEXT,
    create_user TEXT,
    create_time TEXT
);
    ''')

    # app_tags 索引
    run_sql('''
CREATE index IF NOT EXISTS app_tags_index_tag_name on app_tags (tag_name);
    ''')
    run_sql('''
CREATE index IF NOT EXISTS app_tags_index_tag_code on app_tags (tag_code);
    ''')

    # 创建 app_posts_tags
    run_sql('''
    CREATE TABLE IF NOT EXISTS app_posts_tags
(
    id INTEGER primary key autoincrement,
    post_id INTEGER,
    tag_code TEXT,
    create_user TEXT,
    create_time TEXT
);
    ''')

    # app_posts_tags 索引
    run_sql('''
CREATE index IF NOT EXISTS app_posts_tags_index_post_id on app_posts_tags (post_id);
    ''')
    run_sql('''
CREATE index IF NOT EXISTS app_posts_tags_index_tag_code on app_posts_tags (tag_code);
    ''')
