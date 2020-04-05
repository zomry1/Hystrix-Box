import re

hashformat = '^(?:[a-fA-F\d]{32,40})$|^(?:[a-fA-F\d]{52,60})$|^(?:[a-fA-F\d]{92,100})$'

def checkHashFormat(text):
    return bool(re.match(hashformat, text))
