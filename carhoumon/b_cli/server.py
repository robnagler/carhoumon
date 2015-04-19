# -*- coding: utf-8 -*-
"""Starts flask serving :func:`carhoumon.flask_routes`

:copyright: Copyright (c) 2015 Rob Nagler.  All Rights Reserved.
:license: Apache, see LICENSE for more details.
"""
from __future__ import absolute_import, print_function

import json

from flask import Flask
from pybivio import resource

from carhoumon import monitor
from carhoumon import flask_routes

def default_command(port=5000):
    """Runs a flask server on port """
    import sys
    app = Flask(__name__, static_folder=resource.filename('static'))
    flask_routes.init(app)
    app.run(host='0.0.0.0', port=port, debug=True)
