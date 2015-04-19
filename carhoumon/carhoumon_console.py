# -*- coding: utf-8 -*-
"""Runs carhoumon commands. See :mod:`pybivio.pybivio`

:copyright: Copyright (c) 2015 Rob Nagler.  All Rights Reserved.
:license: Apache, see LICENSE for more details.
"""

import sys
import pybivio.cli


def main():
    return pybivio.cli.main('carhoumon')


if __name__ == '__main__':
    sys.exit(main())
