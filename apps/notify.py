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

app_notify = Blueprint('app_notify', __name__)


@app_notify.route("/callback", methods=['POST'])
def notify_callback():
    try:
        print("-----", file=sys.stdout)
        data = request.get_json(force=True)
        print(data, file=sys.stdout)
    except Exception as e:
        traceback.print_exc(e, file=sys.stderr)

    return "ok"


def sge_au99():
    pass
