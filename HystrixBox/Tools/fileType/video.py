from HystrixBox.Tools.fileType.extenstion import Extension


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

    def check(self, header):
        return (len(header) > 4 and
                header[0] == 0x46 and
                header[1] == 0x4C and
                header[2] == 0x56 and
                header[3] == 0x01)


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

    def check(self, header):
        return (len(header) > 4 and
                header[0] == 0x1A and
                header[1] == 0x45 and
                header[2] == 0xDF and
                header[3] == 0xA3)


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

    def check(self, header):
        return (len(header) > 15 and  # Bytes 4-7 is the file size little endian
                header[0] == 0x52 and
                header[1] == 0x49 and
                header[2] == 0x46 and
                header[3] == 0x46 and
                header[8] == 0x41 and
                header[9] == 0x56 and
                header[10] == 0x49 and
                header[11] == 0x20 and
                header[12] == 0x4C and
                header[13] == 0x49 and
                header[14] == 0x53 and
                header[15] == 0x54)


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

    def check(self, header):
        return (len(header) > 10 and
                header[4] == 0x66 and
                header[5] == 0x74 and
                header[6] == 0x79 and
                header[7] == 0x70 and
                header[8] == 0x69 and
                header[9] == 0x73 and
                header[10] == 0x6F and
                header[11] == 0x6D)


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

    def check(self, header):
        return (len(header) > 10 and
                header[3] == 0x66 and
                header[4] == 0x74 and
                header[5] == 0x79 and
                header[6] == 0x70 and
                header[7] == 0x71 and
                header[8] == 0x74 and
                header[9] == 0x20 and
                header[10] == 0x20)


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

    def check(self, header):
        return (len(header) > 10 and
                header[0] == 0x30 and
                header[1] == 0x26 and
                header[2] == 0xB2 and
                header[3] == 0x75 and
                header[4] == 0x8E and
                header[5] == 0x66 and
                header[6] == 0xCF and
                header[7] == 0x11 and
                header[8] == 0xA6 and
                header[9] == 0xD9 and
                header[10] == 0x00 and
                header[11] == 0xAA and
                header[12] == 0x00 and
                header[13] == 0x62 and
                header[14] == 0xCE and
                header[15] == 0x6C)
