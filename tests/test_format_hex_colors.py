#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

from libs.cssformatter import format_hex_colors


def test_lowercase_hex_colors_1():
    code = """
    color:#FFAAEE;
    """
    expected = """
    color:#ffaaee;
    """
    assert (format_hex_colors(code) == expected)


def test_lowercase_hex_colors_2():
    code = """
    color:#fFaAEE;
    """
    expected = """
    color:#ffaaee;
    """
    assert (format_hex_colors(code) == expected)


def test_lowercase_hex_colors_2():
    code = """
    color:#ffaaee;
    """
    expected = """
    color:#ffaaee;
    """
    assert (format_hex_colors(code) == expected)
