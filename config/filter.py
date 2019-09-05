from flask import url_for
from jinja2 import Markup, escape

from config.db import select_list


def menu_tags():

    avail_tags = select_list('''
select at.tag_code as tag_code, tag_name, count(1) as count
from app_tags at,
     app_posts_tags apt
where apt.tag_code = at.tag_code
group by at.tag_code
having count(1) > 0
    ''')

    html = ''

    count = 0
    for avail_tag in avail_tags:
        '''
        <li class="pure-menu-item"><a href="{{ url_for('app_tags.tags', tag_code='python') }}" class="pure-menu-link"><span class="email-label-personal"></span>python</a></li>
        '''
        html += '<li class="pure-menu-item">'

        html += '<a class="pure-menu-link c-label c-label-' + str(count % 5) + '" href="'
        html += url_for('app_tags.tags', tag_code=avail_tag['tag_code'])
        html += '">'

        html += avail_tag['tag_name']
        html += '('
        html += str(avail_tag['count'])
        html += ')'
        html += '</a>'

        html += '</li>'

        count = count + 1

    if count > 0:
        html = '<li class="pure-menu-heading">标签列表</li>' + html

    return Markup(html)

# "{0}{1}{2}{3}{4}".format(
#         escape("My tailor "),
#         "<li>",
#         escape("is"),
#         "</li>",
#         escape(" rich"))
