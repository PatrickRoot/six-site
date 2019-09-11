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


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def run_sql(sql, param):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    print(sql)
    cur.execute(sql, param)

    conn.commit()
    conn.close()


def select_list(sql, param):
    result = []
    conn = sqlite3.connect(db_path)
    conn.row_factory = dict_factory
    cur = conn.cursor()

    for row in cur.execute(sql, param):
        result.append(row)

    conn.close()

    return result


def select_one(sql, param):
    result = []
    conn = sqlite3.connect(db_path)
    conn.row_factory = dict_factory
    cur = conn.cursor()

    for row in cur.execute(sql, param):
        result.append(row)

    conn.close()

    if len(result) > 0:
        return result[0]
    else:
        return None
