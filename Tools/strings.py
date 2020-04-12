import re


def strings(filename, minChars=4):
    regex_string = '[ -~]{' + str(minChars) + ',}'
    try:
        with open(filename, errors='ignore') as f:
            return '\n'.join(re.findall(regex_string, f.read()))
    except FileNotFoundError:
        return ''
