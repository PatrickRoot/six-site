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

import sqlite3

from config.config import db_path


def run_sql(sql):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute(sql)

    conn.commit()
    conn.close()


def run_select(sql):
    result = []
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    for row in c.execute(sql):
        result.append(row)

    conn.close()

    return result
