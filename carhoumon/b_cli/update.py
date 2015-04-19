# -*- coding: utf-8 -*-
"""Calls :func:`carhoumon.monitor.update` with line from argv

:copyright: Copyright (c) 2015 Rob Nagler.  All Rights Reserved.
:license: Apache, see LICENSE for more details.
"""
from __future__ import absolute_import, print_function

import time

from carhoumon import monitor

def default_command(filename, delay=5):
    """Passes lines to update every delay seconds."""
    assert delay >= 1, 'delay must be at least one second'
    lines = []
    with open(filename, 'rb') as f:
        for l in f:
            if not l.startswith('#'):
                lines.append(l)
    for l in lines:
        monitor.update(l)
        time.sleep(delay)
