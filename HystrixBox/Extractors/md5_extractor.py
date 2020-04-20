import re

from HystrixBox.Extractors.extractor import Extractor

MD5_PATTERN = re.compile(r"([a-fA-F\d]{32})")


class MD5Extractor(Extractor):
    """
        A class used to represent an md5 Hash extractor

        .. note:: Regex include both IPv4 and IPv6 formats
    """

    @staticmethod
    def extract(text):
        return MD5_PATTERN.findall(text)
