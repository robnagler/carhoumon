# -*- coding: utf-8 -*-
"""Calls :func:`carhoumon.monitor.update` with line from argv

:copyright: Copyright (c) 2015 Rob Nagler.  All Rights Reserved.
:license: Apache, see LICENSE for more details.
"""
from __future__ import absolute_import, print_function

from carhoumon import monitor

def default_command(line):
    """Passes line to update."""
    monitor.update(line)
