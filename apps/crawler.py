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
import requests
from bs4 import BeautifulSoup

from config.db import run_sql


def sge_au99():
    url = "https://www.sge.com.cn/sjzx/yshqbg"
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3899.0 Safari/537.36 Edg/78.0.275.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(str=r.text, features="html.parser")
    title = soup.select('div.memberName > table > tr:nth-child(2) > td:nth-child(1)')[0].text
    number = soup.select('div.memberName > table > tr:nth-child(2) > td:nth-child(2)')[0].text
    if title == "Au99.99":
        run_sql('''
        insert into app_data(data_code, data_date, data_number) 
        VALUES 
        ('Au99.99', current_timestamp, ?)
        ''', (number,))


def content_fetcher():
    # https://www.fastcompany.com/
    # https://hbr.org/
    # https://www.technologyreview.com/
    # https://www.forbes.com/#6ca64e152254
    #
    pass


def cn_en(str):
    return str


def en_cn(str):
    return str
