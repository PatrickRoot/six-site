from flask import url_for, request
from jinja2 import Markup, escape

from config.db import select_list, select_one


def menu_tags():

    avail_tags = select_list('''
select at.id as tag_id, tag_name, count(1) as count
from app_tags at,
     app_posts_tags apt
where apt.tag_id = at.id
group by at.id
having count(1) > 0
    ''')

    html = ''

    count = 0
    for avail_tag in avail_tags:
        html += '<li class="pure-menu-item">'

        html += '<a class="pure-menu-link c-label c-label-' + str(count % 5) + '" href="'
        html += url_for('app_tags.tags', tag_id=avail_tag['tag_id'])
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


def current_url():
    domain = select_one('''
    select config_val from site_config
    where config_key = 'domain'
    ''')

    request_url = ''
    if domain:
        request_url = domain['config_val']

    request_url = request_url + request.path

    return Markup(request_url)


def register_filter(app):
    env = app.jinja_env
    # env.filters['menu_tags'] = menu_tags
    env.globals["menu_tags"] = menu_tags
    env.globals["current_url"] = current_url
