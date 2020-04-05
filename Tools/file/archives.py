from Tools.file.extenstion import Extension


class Zip(Extension):
    EXTENSION = 'zip'
    MIME = 'application/jpeg'
    DESCRIPTION = 'PKZIP archive file'

    def __init__(self):
        super(Zip, self).__init__(
            extension=Zip.EXTENSION,
            mime=Zip.MIME,
            description=Zip.DESCRIPTION
        )

#50 4B 03 04
    def check(self, buf):
        return (len(buf) > 4 and
                buf[0] == 0x50 and
                buf[1] == 0x4B and
                buf[2] == 0x03 and
                buf[3] == 0x04)
