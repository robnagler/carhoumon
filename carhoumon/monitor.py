# -*- coding: utf-8 -*-
"""Receive updates, normalizes, and stores in db.

:copyright: Copyright (c) 2015 Rob Nagler.  All Rights Reserved.
:license: Apache, see LICENSE for more details.
"""
from __future__ import absolute_import, print_function

import datetime
import errno
import cPickle

DEFAULT_LEVELS = {'last_on': None, 'last_off': None, 'is_on': None}

FIELD_NAMES = ('F1', 'F2', 'R1', 'R2', 'P', 'bP', 'Red', 'Blk', 'STR_V', 'SPR_V', 'HSE_V')

#: This should be absolute (e.g. /var/db/carhoumon/monitor.pickle)
_DB_NAME = 'monitor.pickle'


def current_levels():
    """Returns the current levels as a dict. If no levels, returns empty"""
    try:
        with open(_DB_NAME, 'rb') as f:
            res = cPickle.load(f)
    except IOError as e:
        if e.errno != errno.ENOENT:
            raise
        res = {k: dict(DEFAULT_LEVELS) for k in FIELD_NAMES}
    return res


def parse_date_time(v):
    """Convert date time string to datetime object"""
    # TODO(robnagler) convert to timezone
    return datetime.datetime.strptime(v, '%m/%d/%y %H:%M:%S')


def parse_status_line(line):
    """reads a status line of "date time fields" and returns dict"""
    f = line.split()
    dt = parse_date_time(f.pop(0) + ' ' + f.pop(0))
    res = {k: v == 'ON' for (k, v) in zip(FIELD_NAMES, f)}
    res['date_time'] = dt
    return res


def update(line):
    """Updates db with status line"""
    status = parse_status_line(line)
    curr = current_levels()
    dt = status['date_time']
    for f in FIELD_NAMES:
        c = curr[f]
        if c['is_on'] is None:
            v = dt, dt - datetime.timedelta(0, 1)
            c.update(
                zip(('last_on', 'last_off'),
                    v if status[f] else reversed(v)))
        elif c['is_on'] != status[f]:
            c['last_on' if status[f] else 'last_off'] = dt
        c['is_on'] = status[f]
    with open(_DB_NAME, 'wb') as f:
        cPickle.dump(curr, f)
    return curr
