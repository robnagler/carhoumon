# -*- coding: utf-8 -*-
"""pytest for :mod:`carhoumon.monitor`

:copyright: Copyright (c) 2015 Rob Nagler.  All Rights Reserved.
:license: Apache, see LICENSE for more details.
"""
from __future__ import absolute_import, print_function

import datetime
import pytest
import os
import os.path

from carhoumon import monitor


def test_conformance1():
    """Verify operation with one line"""
    _rm_db()
    curr = monitor.current_levels()
    assert curr['F1'] == monitor.DEFAULT_LEVELS
    #               date     time           F1      F2      R1      R2      P       bP      Red     Blk     STR_V   SPR_V   HSE_V
    monitor.update('04/18/15 09:11:37       ON      OFF     OFF     OFF     OFF     ON      OFF     OFF     OFF     OFF     OFF')
    # This verifies date time parsing as well
    now = datetime.datetime(2015, 4, 18, 9, 11, 37)
    c = monitor.current_levels()
    assert c['F1']['is_on'], \
        'When field turns on, is_on must be true'
    assert c['F1']['last_on'] == now, \
        'When field turns on, last_on must be now'
    assert c['F1']['last_off'] < now, \
        'When field turns on from None, last_off must be at least 1 second before now'
    assert not c['F2']['is_on'], \
        'When field changes from None to off, is_on must be false'
    assert c['F2']['last_on'] < now, \
        'When field changes from None to off, last_on must be before now'
    assert c['F2']['last_off'] == now, \
        'When field changes from None to off, last_off must be now'


def test_conformance2():
    """Read the file and verify status at end"""
    for l in _lines():
        monitor.update(l)
    curr = monitor.current_levels()
    def _assert(field, last_off, last_on):
        d = '04/18/15 '
        expect = {
            'last_off': monitor.parse_date_time(d + last_off),
            'last_on': monitor.parse_date_time(d + last_on),
        }
        expect['is_on'] = expect['last_off'] < expect['last_on']
        assert curr[field] == expect
    _assert('F1', '09:11:36', '09:11:37')
    _assert('F2', '09:11:37', '09:49:03')
    _assert('R1', '09:11:37', '09:31:21')
    _assert('R2', '09:11:37', '09:11:36')
    _assert('P', '09:48:21', '09:44:44')
    _assert('bP', '09:12:39', '09:11:37')


def _rm_db():
    try:
        os.remove(monitor._DB_NAME)
    except OSError:
        pass


def _lines():
    fn = os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)), 'monitor_test.in')
    res = []
    with open(fn) as f:
        for l in f:
            if not l.startswith('#'):
                res.append(l)
    return res
