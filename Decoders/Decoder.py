class Decoder(object):
    @staticmethod
    def validate(self, text):
        raise NotImplementedError

    @staticmethod
    def decode(self, text):
        raise NotImplementedError

    @classmethod
    def safe_decode(cls, text):
        if cls.validate(text):  # Check the text is in the cipher format
            return cls.decode(text)  # Decode it
        else:
            return []  # The text it's not in the format
