import re


def strings(filename, minChars=4):
    """Search printable strings in binary file

    :param filename: The file to be read
    :type filename: str

    :param minChars: Min-len of characters to return string *(default 4)*
    :type minChars: int

    :returns: List of printable strings
    :rtype: list

    """

    regex_string = '[ -~]{' + str(minChars) + ',}'
    try:
        with open(filename, errors='ignore') as f:
            return '\n'.join(re.findall(regex_string, f.read()))
    except FileNotFoundError:
        return ''
