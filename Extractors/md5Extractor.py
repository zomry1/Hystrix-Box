import re

MD5_PATTERN = re.compile(r"([a-fA-F\d]{32})")


def extractMD5(data):
    return MD5_PATTERN.findall(data)
