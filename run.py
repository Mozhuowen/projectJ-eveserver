# -*- coding: utf-8 -*-

"""
    Eve Demo
    ~~~~~~~~

    A demostration of a simple API powered by Eve REST API.

    The live demo is available at eve-demo.herokuapp.com. Please keep in mind
    that the it is running on Heroku's free tier using a free MongoHQ
    sandbox, which means that the first request to the service will probably
    be slow. The database gets a reset every now and then.

    :copyright: (c) 2016 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

import os
import eventhook
from eve import Eve
import controller
import settings
from flask import request,make_response
from werkzeug.contrib.fixers import ProxyFix


# Heroku support: bind to PORT if defined, otherwise default to 5000.
if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    # use '0.0.0.0' to ensure your REST API is reachable from all your
    # network (and not only your computer).
    host = '0.0.0.0'
else:
    port = 5001
    host = '0.0.0.0'


app = Eve()
app.wsgi_app = ProxyFix(app.wsgi_app)
app.on_fetched_item += eventhook.on_fetched_item
app.on_post_GET += eventhook.post_get_callback


@app.route('/action/<action>/<resource>/<item_id>/')
def test_hello(action, resource, item_id):
    return controller.my_action(settings.common_actions.get(action), request, resource, item_id)


@app.route('/test/<id>')
def test(id):
    return controller.test_method(id)


@app.route('/action/<action>', methods=['GET', 'POST'])
def user_action(action):
    return controller.user_action(settings.common_actions.get(action), request)


@app.route('/getfile/<filename>')
def get_file(filename):
    return controller.get_file(filename)


if __name__ == '__main__':
    app.run(host=host, port=port,debug=True)
