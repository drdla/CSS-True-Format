#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Format CSS/SASS/SCSS/LESS code according to LaterPay styleguide.
# Written by Dominik Rodler <drodler@laterpay.net>
#
# usage:
#   format_code(code)
#
"""
Format CSS/SASS/SCSS/LESS code according to LaterPay styleguide.
"""
from __future__ import unicode_literals, print_function, absolute_import


import re


def format_code(code):
    code = normalize_code(code)
    code = apply_LaterPay_style(code)

    return code


def normalize_code(code):
    code = remove_invalid_selectors(code)
    code = trim_whitespace(code)
    code = replace_tabs_with_spaces(code)
    code = replace_nonspace_whitespaces_with_newlines(code)
    code = remove_whitespace_around_some_special_characters(code)
    code = remove_whitespace_before_closing_curly_braces(code)
    # this might break handling of comments:
    # code = remove_newline_after_closing_curly_braces(code)
    code = remove_spaces_between_newlines(code)
    code = add_missing_semicolons(code)
    code = remove_superfluous_semicolons(code)

    return code


def apply_LaterPay_style(code):
    code = add_space_around_selector_characters(code)

    code = add_space_before_opening_curly_braces(code)
    code = remove_space_after_opening_curly_braces(code)
    code = add_newline_at_beginning_of_media_ruleset(code)
    code = add_newline_after_charset_and_import(code)
    code = add_newline_before_included_selectors(code)

    code = remove_whitespace_before_closing_curly_braces(code)
    code = add_newline_after_closing_curly_braces(code)

    code = remove_excess_newlines(code)

    code = add_space_after_semicolon(code)
    code = remove_space_after_colon(code)
    code = handle_whitespace_after_comma(code)

    code = replace_double_quotes_with_single_quotes(code)
    code = remove_quotes_within_urls(code)

    code = fix_space_after_http(code)
    code = fix_data_uris(code)

    code = strip_leading_zeros_from_values(code)
    code = fix_0_values(code)

    code = add_space_before_important(code)

    code = format_hex_colors(code)

    code = handle_comments(code)

    code = sort_properties(code)
    code = expand_long_rules(code)
    code = indent_rules(code)

    code = add_newline_at_end_of_file(code)

    return code


def trim_whitespace(code):
    code = code.strip()

    return code


def replace_tabs_with_spaces(code):
    code = re.sub(r'\t', '    ', code)

    return code


def replace_nonspace_whitespaces_with_newlines(code):
    code = re.sub(r'[\r\f\v]', '\n', code)

    return code


def remove_newline_after_closing_curly_braces(code):
    code = re.sub(r'(\})\n', r'\1', code)

    return code


def add_newline_after_closing_curly_braces(code):
    code = re.sub(r'\}', r'}\n', code)

    return code


def add_space_before_opening_curly_braces(code):
    code = re.sub(r'(\S)\{', r'\1 {', code)

    return code


def remove_space_after_opening_curly_braces(code):
    code = re.sub(r'{(\s)(\S)', r'{\2', code)

    return code


def remove_whitespace_before_closing_curly_braces(code):
    code = re.sub(r'\s*(\})', r'\1', code)

    return code


def remove_whitespace_around_some_special_characters(code):
    # remove \s before and after {:;,
    code = re.sub(r'\s*([\{:;,])\s*', r'\1', code)

    return code


def remove_spaces_between_newlines(code):
    code = re.sub(r'\n[ ]+\n', r'\n\n', code)

    return code


def remove_excess_newlines(code):
    # preserve up to 2 consecutive empty lines
    code = re.sub(r'\n{3,}', r'\n\n\n', code)

    return code


def remove_space_after_colon(code):
    code = re.sub(r'\s*([\:])\s*', r'\1', code)

    return code


def add_space_after_semicolon(code):
    # add space after ; except for before }
    code = re.sub(r'(\S);([^\}])', r'\1; \2', code)

    return code


def replace_double_quotes_with_single_quotes(code):
    code = code.replace('"', '\'')

    return code


def remove_invalid_selectors(code):
    code = re.sub(r',[\d\s\.\#\+>:]*\{', '{', code)

    return code


def remove_quotes_within_urls(code):
    code = re.sub(r'url\(\'([^\)]+)\'\)', r'url(\1)', code)

    return code


def handle_whitespace_after_comma(code):
    # add space or \n after ,
    block = code.split('}')

    for i in range(len(block)):
        b = block[i].split('{')
        for j in range(len(b)):
            if b[j].count('@import'):
                s = b[j].split(';')
                for k in range(len(s)):
                    # ignore @import
                    if not s[k].count('@import'):
                        s[k] = re.sub(r',(\S)', r',\n\1', s[k])
                b[j] = ';'.join(s)
            else:
                if j == len(b) - 1 or b[j].count('@media'):
                    # add space after properties' or @media's ,
                    b[j] = re.sub(r',(\S)', r', \1', b[j])
                else:
                    # add \n between multiple selectors after ,
                    b[j] = re.sub(r',(\S)', r',\n\1', b[j])
        block[i] = '{'.join(b)
    code = '}'.join(block)

    return code


def remove_superfluous_semicolons(code):
    code = re.sub(r';\s*;', ';', code)

    return code


def add_missing_semicolons(code):
    code = re.sub(r'([^;])\}', r'\1;}', code)

    return code


def handle_comments(code):
    # add space before and after comment content
    code = re.sub(r'\/\*\s*([\s\S]+?)\s*\*\/', r'/* \1 */', code)
    # code = re.sub(r'\}\s*(\/\*[\s\S]+?\*\/)\s*', r'}\n\1\n', code)
    # add \n before and after outside comment
    # fix comment after ;
    code = re.sub(r'\;\s*(\/\*[^\n]*\*\/)\s*', r'; \1\n', code)
    # remove \n between comment and }
    # code = re.sub(r'(\/\*[^\n]*\*\/)\s+\}', r'\1}', code)

    return code


def sort_properties(code):
    lines = code.split('\n')

    for i in range(len(lines)):
        # get CSS rule by trimming current line
        rule = lines[i].strip()

        # extract CSS selector from rule
        selectorEnd = rule.find('{')
        if selectorEnd > 0:
            selector = rule[:selectorEnd]
            # delete selector from rule
            propertiesStart = selectorEnd + 1
            rule = rule[propertiesStart:]
            rule = re.sub(r'\}', r'', rule)

            # sort CSS properties alphabetically
            properties = re.sub(r';\s', r';', rule).split(';')
            properties = filter(None, properties)

            # custom sorting required in order to not chanage the sequence
            # of properties in a way that affects appearance
            # : must be sorted higher than -
            # TODO: make sure e.g. border-width: is sorted after border:
            properties = sorted(properties, key=lambda x: x.replace(':', 'a'))

            # reconstruct rule
            rule = selector + '{' + '; '.join(properties) + ';}'

        lines[i] = rule

    code = '\n'.join(lines)

    return code


def expand_long_rules(code):
    # expand rules that exceed a given line length
    expand_threshold = 120
    lines = code.split('\n')

    for i in range(len(lines)):
        if (expand_threshold < len(lines[i])):
            # add \n after {
            lines[i] = re.sub(r'\{(\S)', r'{\n\1', lines[i])
            # add \n and indentation after ; except for ; before }
            lines[i] = re.sub(r'(\S);([^\}])', r'\1;\n    \2', lines[i])
            # add \n before }
            lines[i] = re.sub(r'([^\}])\s*\}', r'\1\n}', lines[i])

    code = '\n'.join(lines)

    return code


def indent_rules(code):
    lines = code.split('\n')
    level = 0
    tabSize = 4
    spaces = ' ' * tabSize

    for i in range(len(lines)):
        increment = lines[i].count('{') - lines[i].count('}')
        level = level + increment
        thisLevel = level - increment if increment > 0 else level
        lines[i] = lines[i].strip()
        lines[i] = spaces * thisLevel + lines[i]

    code = '\n'.join(lines)

    return code


def add_space_around_selector_characters(code):
    code = re.sub(r'(\S)([>+])', r'\1 \2', code)  # add space before > +
    code = re.sub(r'([>+])(\S)', r'\1 \2', code)  # add space after > +

    return code


def fix_space_after_http(code):
    code = re.sub(r'(http[s]?:) \/\/', r'\1//', code)

    return code


def fix_data_uris(code):
    # TODO: remove \s inserted into data URIs by other formatting

    return code


def strip_leading_zeros_from_values(code):
    # remove 0 from 0.x values directly after colon
    code = re.sub(r':0\.', r':.', code)

    return code


def fix_0_values(code):
    # remove unit from 0 values after \s or colon
    code = re.sub(r'([\s:])0[emprx%]+', r'\g<1>0', code)

    return code


def format_hex_colors(code):
    hexColor = re.compile(r'#([0-9a-fA-F]{3,6})')

    for hexValue in hexColor.finditer(code):
        # lowercase hex colors
        # TODO: make sure ID selectors are not processed
        hexValueNew = hexValue.group(1).lower()
        # if len(hexValueNew) == 6
        # hexValueNew = re.sub(r'(\w)\1(.)\2(.)\3', r'\1\2\3', hexValueNew) #
        # compress 6-digit values to 3-digit values
        code = code.replace(hexValue.group(1), hexValueNew)

    return code


def add_space_before_important(code):
    code = re.sub(r'\s*!important', ' !important', code)

    return code


def add_newline_before_included_selectors(code):
    code = re.sub(r';\s*([^\};]+?\{)', r';\n\1', code)

    return code


def add_newline_at_beginning_of_media_ruleset(code):
    code = re.sub(r'((@media|@[\w-]*keyframes)[^\{]+\{)\s*', r'\1\n', code)

    return code


def add_newline_after_charset_and_import(code):
    code = re.sub(r'((?:@charset|@import)[^;]+;)\s*', r'\1\n', code)

    return code


def add_newline_at_end_of_file(code):
    code = trim_whitespace(code)
    code = code + '\n'

    return code
