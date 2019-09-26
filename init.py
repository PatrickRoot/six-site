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
from config.db import select_one, run_sql


def add_update_config(key, val, replace):
    site_config = select_one('''
                  select *
                  from site_config
                  where config_key = ?
                  ''', (key,))

    if not site_config:
        run_sql('''
        INSERT INTO site_config 
        (config_key, config_val) 
        VALUES 
        (?, ?);
        ''', (key, val))
    elif replace:
        run_sql('''
        UPDATE site_config 
        SET config_val = ?
        WHERE config_key = ?
        ''', (val, key))


if __name__ == '__main__':
    add_update_config("domain", "", False)
    add_update_config("telegram.url", "", False)
    add_update_config("telegram.token", "", False)
    add_update_config("mine.help", "", False)
