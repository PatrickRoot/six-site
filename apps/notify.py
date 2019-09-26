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
import sys
import traceback

from flask import Blueprint, request

from config.db import select_one
from config.tele import send_msg

app_notify = Blueprint('app_notify', __name__)


def send_my_help(chat_id):
    site_config = select_one('''
    select *
    from site_config
    where config_key = 'mine.help'
    ''', ())
    send_msg(chat_id, site_config.config_val)


@app_notify.route("/callback", methods=['POST'])
def notify_callback():
    try:
        print("-----")
        data = request.get_json(force=True)
        print(data, file=sys.stdout)

        if data['message']['text'] == '/help':
            if data['chat']['id'] in (624880292, 463360558):
                send_my_help(data['chat']['id'])

    except Exception as e:
        traceback.print_exc(file=sys.stderr)

    return "ok"


def sge_au99():
    pass
