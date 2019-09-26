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

from flask import Blueprint, render_template

from config.db import select_list

app_notes = Blueprint('app_notes', __name__)


@app_notes.route("/group")
def notes_group():
    group_list = select_list('''
    select note_group as group_name
    from app_notes
    group by note_group
    order by note_group
    ''', ())
    return render_template('notes/group.html',
                           group_list=group_list)
                           # url_prefix=url_prefix,
                           # page_no=page_num,
                           # begin=begin,
                           # end=end,
                           # total_num=total_number,
                           # total_page=total_page)


@app_notes.route("/list/<string:group_name>")
def notes_list(group_name):
    note_list = select_list('''
    select *
    from app_notes
    where note_group = ?
    order by note_order
    ''', (group_name,))
    return render_template('notes/list.html',
                           note_list=note_list,
                           group_name=group_name)
