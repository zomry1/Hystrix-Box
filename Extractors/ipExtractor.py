import re

IPv4_PATTERN = re.compile(
    "(?:(?:1\d\d|2[0-5][0-5]|2[0-4]\d|0?[1-9]\d|0?0?\d)\.){3}(?:1\d\d|2[0-5][0-5]|2[0-4]\d|0?[1-9]\d|0?0?\d)")

IPv6_PATTERN = re.compile('\b(?:[a-f0-9]{1,4}:|:){2,7}(?:[a-f0-9]{1,4}|:)\b', re.IGNORECASE | re.VERBOSE)


def extractIP(data):
    # It's more efficent to use 2 patterns instead use OR between 2 regex
    ips = IPv4_PATTERN.findall(data)
    ips += IPv6_PATTERN.findall(data)
    return ips

