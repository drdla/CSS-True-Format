#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

from libs.cssformatter import sort_properties


def test_prefixes_first():
    code = """
    -webkit-border-radius:3px; border-radius:3px; -moz-border-radius:3px;
    """
    expected = """
    -moz-border-radius:3px; -webkit-border-radius:3px; border-radius:3px;
    """
    assert (sort_properties(code) == expected)
