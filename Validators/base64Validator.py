import re

base64Format = '^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$'

def checkBase64Format(text):
    return bool(re.match(base64Format, text))

