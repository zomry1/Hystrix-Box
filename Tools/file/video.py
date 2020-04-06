from Tools.file.extenstion import Extension


class Flv(Extension):
    EXTENSION = 'flv'
    MIME = 'video/x-flv'
    DESCRIPTION = 'Flash video file'

    def __init__(self):
        super(Flv, self).__init__(
            extension=Flv.EXTENSION,
            mime=Flv.MIME,
            description=Flv.DESCRIPTION
        )

    def check(self, buf):
        return (len(buf) > 4 and
                buf[0] == 0x46 and
                buf[1] == 0x4C and
                buf[2] == 0x56 and
                buf[3] == 0x01)


class Matroska(Extension):
    EXTENSION = 'mkv (webm)'
    MIME = 'video/x-matroska'
    DESCRIPTION = 'Matroska stream file'

    def __init__(self):
        super(Matroska, self).__init__(
            extension=Matroska.EXTENSION,
            mime=Matroska.MIME,
            description=Matroska.DESCRIPTION
        )

    def check(self, buf):
        return (len(buf) > 4 and
                buf[0] == 0x1A and
                buf[1] == 0x45 and
                buf[2] == 0xDF and
                buf[3] == 0xA3)


class Avi(Extension):
    EXTENSION = 'avi'
    MIME = 'video/x-msvideo'
    DESCRIPTION = '	Resource Interchange File Format -- Windows Audio Video Interleave file'

    def __init__(self):
        super(Avi, self).__init__(
            extension=Avi.EXTENSION,
            mime=Avi.MIME,
            description=Avi.DESCRIPTION
        )

    def check(self, buf):
        return (len(buf) > 15 and  # Bytes 4-7 is the file size little endian
                buf[0] == 0x52 and
                buf[1] == 0x49 and
                buf[2] == 0x46 and
                buf[3] == 0x46 and
                buf[8] == 0x41 and
                buf[9] == 0x56 and
                buf[10] == 0x49 and
                buf[11] == 0x20 and
                buf[12] == 0x4C and
                buf[13] == 0x49 and
                buf[14] == 0x53 and
                buf[15] == 0x54)


class Mp4(Extension):
    EXTENSION = 'mp4'
    MIME = 'video/mp4'
    DESCRIPTION = 'MPEG-4 video file'

    def __init__(self):
        super(Mp4, self).__init__(
            extension=Mp4.EXTENSION,
            mime=Mp4.MIME,
            description=Mp4.DESCRIPTION
        )

    def check(self, buf):
        return (len(buf) > 10 and
                buf[3] == 0x66 and
                buf[4] == 0x74 and
                buf[5] == 0x79 and
                buf[6] == 0x70 and
                buf[7] == 0x69 and
                buf[8] == 0x73 and
                buf[9] == 0x6F and
                buf[10] == 0x6D)

class Mov(Extension):
    EXTENSION = 'mov'
    MIME = 'video/quicktime'
    DESCRIPTION = 'QuickTime movie file'

    def __init__(self):
        super(Mov, self).__init__(
            extension=Mov.EXTENSION,
            mime=Mov.MIME,
            description=Mov.DESCRIPTION
        )

    def check(self, buf):
        return (len(buf) > 10 and
                buf[3] == 0x66 and
                buf[4] == 0x74 and
                buf[5] == 0x79 and
                buf[6] == 0x70 and
                buf[7] == 0x71 and
                buf[8] == 0x74 and
                buf[9] == 0x20 and
                buf[10] == 0x20)


class Wmv(Extension):
    EXTENSION = 'wmv'
    MIME = 'video/x-ms-wmv'
    DESCRIPTION = 'Microsoft Windows Media Audio/Video File'

    def __init__(self):
        super(Wmv, self).__init__(
            extension=Wmv.EXTENSION,
            mime=Wmv.MIME,
            description=Wmv.DESCRIPTION
        )

    def check(self, buf):
        return (len(buf) > 10 and
                buf[0] == 0x30 and
                buf[1] == 0x26 and
                buf[2] == 0xB2 and
                buf[3] == 0x75 and
                buf[4] == 0x8E and
                buf[5] == 0x66 and
                buf[6] == 0xCF and
                buf[7] == 0x11 and
                buf[8] == 0xA6 and
                buf[9] == 0xD9 and
                buf[10] == 0x00 and
                buf[11] == 0xAA and
                buf[12] == 0x00 and
                buf[13] == 0x62 and
                buf[14] == 0xCE and
                buf[15] == 0x6C)