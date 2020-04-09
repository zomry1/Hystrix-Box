import re
from Extractors.Extractor import Extractor

MD5_PATTERN = re.compile(r"([a-fA-F\d]{32})")


class MD5Extractor(Extractor):
    @staticmethod
    def extract(text):
        return MD5_PATTERN.findall(text)
