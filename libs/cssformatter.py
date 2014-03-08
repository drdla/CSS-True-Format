#
# Format CSS/SASS/SCSS/LESS code according to LaterPay styleguide.
#   written by Dominik Rodler <drodler@laterpay.net>
#
# usage:
#   format_code(code, action)
#

"""Format CSS/SASS/SCSS/LESS code according to LaterPay styleguide."""

import re

def format_code(code):
    code = normalize_code(code)
    code = apply_LaterPay_style(code)
    code = trim(code)

    return code

def normalize_code(code):
    code = re.sub(r'\s*([\{\}:;,])\s*', r'\1', code)                        # remove \s before and after characters {}:;,
    code = re.sub(r'\n', r'', code)                                         # remove \n
    code = re.sub(r',[\d\s\.\#\+>:]*\{', '{', code)                         # remove invalid selectors
    code = re.sub(r';\s*;', ';', code)                                      # remove superfluous ;

    code = re.sub(r'\/\*\s*([\s\S]+?)\s*\*\/', r'/* \1 */', code)           # add space before and after comment content
    code = re.sub(r'\}\s*(\/\*[\s\S]+?\*\/)\s*', r'}\n\1\n', code)          # add \n before and after outside comment
    code = re.sub(r'(http[s]?:) \/\/', r'\1//', code)                       # fix space after http[s]:
    code = re.sub(r'\s*!important', ' !important', code)                    # add space before !important

    return code

def apply_LaterPay_style(code):
    code = fix_0_values(code)

    code = re.sub(r'(\S)\{', r'\1 {', code)                                 # add space before {
    code = re.sub(r'{(\s)(\S)', r'{\2', code)                               # remove space after {
    code = re.sub(r'((@media|@[\w-]*keyframes)[^\{]+\{)\s*', r'\1\n', code) # add \n after @media {

    code = re.sub(r'\s*([\:])\s*', r'\1', code)                             # remove space after :
    code = re.sub(r'(\S);([^\}])', r'\1; \2', code)                         # add space after ;
    code = re.sub(r'\;\s*(\/\*[^\n]*\*\/)\s*', r'; \1\n', code)             # fix comment after ;
    code = re.sub(r'((?:@charset|@import)[^;]+;)\s*', r'\1\n', code)        # add \n after @charset & @import
    code = re.sub(r';\s*([^\};]+?\{)', r';\n\1', code)                      # add \n before included selector

    # TODO: add space around > + /
    # TODO: add space around *, if at least one adjacent character is a number (in order to preserve hacks)
    # TODO: remove " or ' with url(...)
    # TODO: compress hex color values

    code = re.sub(r'(\/\*[^\n]*\*\/)\s+\}', r'\1}', code)                   # remove \n between comment and }
    code = re.sub(r'(\s)\}', r'\1}', code)                                  # remove space before }
    code = re.sub(r'([^;])\}', r'\1;}', code)                               # add missing ; before }
    code = re.sub(r'\}\s*', r'}\n', code)                                   # add \n after }

    code = comma_rules(code)                                                # add space or \n after ,
    code = sort_properties(code)
    code = expand_long_rules(code)
    code = indent_rules(code)

    return code

def comma_rules(code):
    block = code.split('}')

    for i in range(len(block)):
        b = block[i].split('{')
        for j in range(len(b)):
            if b[j].count('@import'):
                s = b[j].split(';')
                for k in range(len(s)):
                    if not s[k].count('@import'):                           # ignore @import
                        s[k] = re.sub(r',(\S)', r',\n\1', s[k])
                b[j] = ';'.join(s)
            else:
                if j == len(b) - 1 or b[j].count('@media'):
                    b[j] = re.sub(r',(\S)', r', \1', b[j])                  # add space after properties' or @media's ,
                else:
                    b[j] = re.sub(r',(\S)', r',\n\1', b[j])                 # add \n after selectors' ,
        block[i] = '{'.join(b)
    code = '}'.join(block)

    return code

def sort_properties(code):
    lines = code.split('\n')

    for i in range(len(lines)):
        # get CSS rule by trimming current line
        rule = trim(lines[i])

        # extract CSS selector from rule
        selectorCharacters = rule.find('{')
        if selectorCharacters > 0:
            selector = rule[:selectorCharacters]
            # delete selector from rule
            rule = re.sub(r'(\S*\s*\{)', r'', rule)
            rule = re.sub(r'\}', r'', rule)

            # sort CSS properties alphabetically
            properties = re.sub(r';\s', r';', rule).split(';')
            properties = filter(None, properties)
            properties = sorted(properties)

            rule = selector + '{' + '; '.join(properties) + ';}'            # reconstruct rule

        lines[i] = rule

    code = '\n'.join(lines)

    return code

def expand_long_rules(code):
    expand_threshold = 120  # expand rules with > 120 charactes
# TODO: make this a setting
    lines = code.split('\n')

    for i in range(len(lines)):
        if (expand_threshold < len(lines[i])):
            lines[i] = re.sub(r'\{(\S)', r'{\n\1', lines[i])                # add \n after {
            lines[i] = re.sub(r'(\S);([^\}])', r'\1;\n    \2', lines[i])    # add \n and indentation after ; except for ; before }
            lines[i] = re.sub(r'([^\}])\s*\}', r'\1\n}', lines[i])          # add \n before }

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
        lines[i] = trim(lines[i])
        lines[i] = spaces * thisLevel + lines[i]

    code = '\n'.join(lines)

    return code

def trim(code):
    code = re.sub(r'^\s*(\S+(\s+\S+)*)\s*$', r'\1', code)

    return code

def fix_0_values(code):
    code = re.sub(r'\s0[emprtx%]+', r' 0', code)                            # remove unit from 0 values after \s
    code = re.sub(r':0[emprtx%]+', r':0', code)                             # remove unit from 0 values after :

    return code
