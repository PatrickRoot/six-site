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
import os

from flask import Blueprint, render_template, jsonify, request

from config.db import select_one, select_list, run_sql2
from config.utils import is_login

app_api = Blueprint('app_api', __name__)


@app_api.route("/")
def thought_index():
    return "api"


def import_md(filename):
    file_object = open(filename, 'rU')
    count = 0
    is_list = False

    try:
        origin_id = ""
        title = ""
        date = ""
        content_origin = ""
        tags = []

        for line in file_object:
            line_strip = line.strip()
            if line_strip == "---":
                count = count + 1
                continue
            if count > 1:
                content_origin = content_origin + line
                continue

            if line_strip.startswith("id:"):
                id = line_strip.replace("id:", "", 1).strip()
                continue
            if line_strip.startswith("title:"):
                title = line_strip.replace("title:", "", 1).strip()
                continue
            if line_strip.startswith("date:"):
                date = line_strip.replace("date:", "", 1).strip()
                continue
            if line_strip.startswith("- "):
                tag = line_strip.replace("- ", "", 1).strip()
                tags.append(tag)
                continue

        run_sql2('''
        INSERT INTO app_posts 
        (post_type, post_title, post_summary, post_content, post_content_origin, post_status, view_count, thumb_count, comment_count, create_user, create_time) 
        VALUES 
        ('blog', ?, ?, ?, ?, '1', 0, 0, 0, ?, ?)
        ''', (title, id, 'todo', content_origin, 'import', date))

        app_posts = select_one('''
        select *
        from app_posts
        where post_summary = '%s'
        ''' % (id,))

        if app_posts:
            post_id = app_posts["id"]

            for tag_name in tags:
                app_tags = select_one('''
                select *
                from app_tags
                where tag_name = '%s'
                ''' % tag_name)

                if not app_tags:
                    run_sql2('''
                    INSERT INTO app_tags 
                    (tag_name) 
                    VALUES 
                    (?);
                    ''', (tag_name,))

                    app_tags = select_one('''
                                select *
                                from app_tags
                                where tag_name = '%s'
                                ''' % tag_name)

                run_sql2('''
                INSERT INTO app_posts_tags
                (post_id, tag_id) 
                VALUES 
                (?, ?)
                ''', (post_id, app_tags["id"]))

    finally:
        file_object.close()


@app_api.route("/import/wordpress", methods=['GET', 'POST'])
def import_wordpress():
    hexo_path = '/Users/patrickroot/six_myspace/python/six-site/test'
    if request.args.__contains__("path"):
        hexo_path = request.args

    if request.form.__contains__("path"):
        hexo_path = request.form['path']

    if hexo_path:
        for filename in os.listdir(hexo_path):
            filename = os.path.join(hexo_path, filename)
            if filename.endswith(".md") and os.path.isfile(filename):
                import_md(filename)

    return jsonify({

    })


'''
---
title: Centos 7 开发环境之 Gogs 的安装及配置（二进制）
id: 2018/06/07/gogs
date: 2018-06-07 12:44:32
categories:
  - 技术研究
tags:
  - centos
  - Gogs
  - Git
toc: true
comments: true
---

'''