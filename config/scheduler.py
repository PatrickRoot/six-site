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
from apps import crawler


def add_jobs(scheduler):
    scheduler.add_job(id="sge_au99", func=crawler.sge_au99, trigger='cron', minute='*/5')


def sge_au99():
    """
          *                  any     Fire on every value
          */a               any     Fire every a values, starting from the minimum
          a-b              any     Fire on any value within the a-b range (a must be smaller than b)
          a-b/c           any     Fire every c values within the a-b range
          xth y            day     Fire on the x -th occurrence of weekday y within the month
          last x           day     Fire on the last occurrence of weekday x within the month
          last              day     Fire on the last day within the month
          x,y,z             any     Fire on any matching expression; can combine any number of any of the above
    """
