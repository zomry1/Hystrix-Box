from Tools.file.extenstion import Extension


# https://www.iana.org/assignments/media-types/font/otf
class Otf(Extension):  # Print version = print(buf[5:8])
    EXTENSION = 'otf'
    MIME = 'font/otf'
    DESCRIPTION = 'OpenType font file'

    def __init__(self):
        super(Otf, self).__init__(
            extension=Otf.EXTENSION,
            mime=Otf.MIME,
            description=Otf.DESCRIPTION
        )

    def check(self, header):
        return (len(header) > 5 and
                header[0] == 0x4F and
                header[1] == 0x54 and
                header[2] == 0x54 and
                header[3] == 0x4F and
                header[4] == 0x00)


# https://www.iana.org/assignments/media-types/font/ttf
class Ttf(Extension):  # Print version = print(buf[5:8])
    EXTENSION = 'ttf'
    MIME = 'font/ttf'
    DESCRIPTION = 'TrueType font file'

    def __init__(self):
        super(Ttf, self).__init__(
            extension=Ttf.EXTENSION,
            mime=Ttf.MIME,
            description=Ttf.DESCRIPTION
        )

    def check(self, header):
        return (len(header) > 5 and
                header[0] == 0x74 and
                header[1] == 0x72 and
                header[2] == 0x75 and
                header[3] == 0x65 and
                header[4] == 0x00)
