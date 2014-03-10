#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

from libs.cssformatter import sort_properties


def test_prefixes_first():
    code = """
    -some stuff
    """
    expected = """
    -some otherstuff
    """
    assert (sort_properties(code) == expected)
