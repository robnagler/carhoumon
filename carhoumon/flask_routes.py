# -*- coding: utf-8 -*-
"""Serve up some flask routes. We setup routes manually.

:copyright: Copyright (c) 2015 Rob Nagler.  All Rights Reserved.
:license: Apache, see LICENSE for more details.
"""
from __future__ import absolute_import, print_function

import flask
import json

from carhoumon import monitor


def init(app):
    """Initialize all the routes"""
    app.add_url_rule('/', view_func=home)
    app.add_url_rule('/current_levels', view_func=current_levels)


def current_levels():
    """Return current_levels as json"""
    return flask.jsonify(monitor.current_levels())

def home():
    """Return static index.html"""
    return flask.current_app.send_static_file('index.html')
