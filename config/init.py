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
)
    ''',())

    # site_config 索引
    run_sql('''
CREATE index IF NOT EXISTS site_config_index_config_key on site_config (config_key)
    ''',())

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
)
    ''',())

    # app_posts 索引
    run_sql('''
CREATE index IF NOT EXISTS app_posts_index_post_type on app_posts (post_type)
    ''',())

    run_sql('''
CREATE index IF NOT EXISTS app_posts_index_post_status on app_posts (post_status)
    ''',())

    # 创建 app_tags
    run_sql('''
    CREATE TABLE IF NOT EXISTS app_tags
(
    id INTEGER primary key autoincrement,
    tag_name TEXT,
    create_user TEXT,
    create_time TEXT
)
    ''',())

    # app_tags 索引
    run_sql('''
CREATE index IF NOT EXISTS app_tags_index_tag_name on app_tags (tag_name)
    ''',())

    # 创建 app_posts_tags
    run_sql('''
    CREATE TABLE IF NOT EXISTS app_posts_tags
(
    id INTEGER primary key autoincrement,
    post_id INTEGER,
    tag_id INTEGER,
    create_user TEXT,
    create_time TEXT
)
    ''',())

    # app_posts_tags 索引
    run_sql('''
CREATE index IF NOT EXISTS app_posts_tags_index_post_id on app_posts_tags (post_id)
    ''',())
    run_sql('''
CREATE index IF NOT EXISTS app_posts_tags_index_tag_id on app_posts_tags (tag_id)
    ''',())

    # 创建 app_user
    run_sql('''
    CREATE TABLE IF NOT EXISTS app_user
(
    id INTEGER primary key autoincrement,
    username INTEGER,
    password TEXT,
    bio TEXT,
    intro TEXT,
    create_user TEXT,
    create_time TEXT
)
    ''',())

    # app_user 索引
    run_sql('''
CREATE index IF NOT EXISTS app_user_index_username on app_user (username)
    ''',())

    # 创建 app_comment
    run_sql('''
    CREATE TABLE IF NOT EXISTS app_comment
(
    id INTEGER primary key autoincrement,
    post_id INTEGER,
    reply_id INTEGER,
    reply_count INTEGER,
    thumb_count INTEGER,
    comment_content TEXT,
    create_user TEXT,
    create_time TEXT
)
    ''',())

    # app_comment 索引
    run_sql('''
CREATE index IF NOT EXISTS app_comment_index_post_id on app_comment (post_id)
    ''',())
    run_sql('''
CREATE index IF NOT EXISTS app_comment_index_reply_id on app_comment (reply_id)
    ''',())

    # 创建 app_data
    run_sql('''
    CREATE TABLE IF NOT EXISTS app_data
(
    id INTEGER primary key autoincrement,
    data_code TEXT,
    data_date TEXT,
    data_number TEXT,
    create_user TEXT,
    create_time TEXT
)
    ''', ())

    # app_comment 索引
    run_sql('''
CREATE index IF NOT EXISTS app_data_index_data_code on app_data (data_code)
    ''', ())
    run_sql('''
CREATE index IF NOT EXISTS app_data_index_data_date on app_data (data_date)
    ''', ())

    # 创建 app_data
    run_sql('''
    CREATE TABLE IF NOT EXISTS app_notify_config
(
    id INTEGER primary key autoincrement,
    notify_code TEXT,
    notify_type TEXT,
    notify_number INTEGER,
    create_user TEXT,
    create_time TEXT
)
    ''', ())
    # notify_type：100 单次涨幅 101 涨幅上限 200 单次跌幅 201 跌幅下限

    # app_comment 索引
    run_sql('''
CREATE index IF NOT EXISTS app_notify_config_index_notify_code on app_notify_config (notify_code)
    ''', ())
    run_sql('''
CREATE index IF NOT EXISTS app_notify_config_index_notify_type on app_notify_config (notify_type)
    ''', ())

    # 创建 app_notes
    run_sql('''
    CREATE TABLE IF NOT EXISTS app_notes
(
    id INTEGER primary key autoincrement,
    note_group TEXT,
    note_content TEXT,
    note_order INTEGER,
    create_user TEXT,
    create_time TEXT
)
    ''', ())
    # notify_type：100 单次涨幅 101 涨幅上限 200 单次跌幅 201 跌幅下限

    # app_comment 索引
    run_sql('''
CREATE index IF NOT EXISTS app_notes_index_note_group on app_notes (note_group)
    ''', ())
