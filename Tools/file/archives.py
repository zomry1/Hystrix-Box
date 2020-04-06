from Tools.file.extenstion import Extension


# https://www.iana.org/assignments/media-types/application/zip
class Zip(Extension):
    EXTENSION = 'zip'
    MIME = 'application/zip'
    DESCRIPTION = 'PKZIP archive file'

    def __init__(self):
        super(Zip, self).__init__(
            extension=Zip.EXTENSION,
            mime=Zip.MIME,
            description=Zip.DESCRIPTION
        )

    def check(self, buf):
        return (len(buf) > 4 and
                buf[0] == 0x50 and
                buf[1] == 0x4B and
                buf[2] == 0x03 and
                buf[3] == 0x04)


# https://www.iana.org/assignments/media-types/application/vnd.rar
class Rar(Extension):
    EXTENSION = 'rar'
    MIME = 'application/vdn.rar'
    DESCRIPTION = 'RAR archive'

    def __init__(self):
        super(Rar, self).__init__(
            extension=Rar.EXTENSION,
            mime=Rar.MIME,
            description=Rar.DESCRIPTION
        )

    def check(self, buf):
        return (len(buf) > 8 and  # first is v4 and the second is v5
                (buf[0] == 0x52 and
                 buf[1] == 0x61 and
                 buf[2] == 0x72 and
                 buf[3] == 0x21 and
                 buf[4] == 0x1A and
                 buf[5] == 0x07 and
                 buf[6] == 0x00)
                or
                (buf[0] == 0x52 and
                 buf[1] == 0x61 and
                 buf[2] == 0x72 and
                 buf[3] == 0x21 and
                 buf[4] == 0x1A and
                 buf[5] == 0x07 and
                 buf[6] == 0x01 and
                 buf[7] == 0x00))


class Sevenz(Extension):
    EXTENSION = '7z'
    MIME = 'application/x-7z-compressed'
    DESCRIPTION = '7-Zip File Format'

    def __init__(self):
        super(Sevenz, self).__init__(
            extension=Sevenz.EXTENSION,
            mime=Sevenz.MIME,
            description=Sevenz.DESCRIPTION
        )

    def check(self, buf):
        return (len(buf) > 6 and
                buf[0] == 0x37 and
                buf[1] == 0x7A and
                buf[2] == 0xBC and
                buf[3] == 0xAF and
                buf[4] == 0x27 and
                buf[5] == 0x1C)



class Jar(Extension):
    EXTENSION = 'jar'
    MIME = 'application/java-archive'
    DESCRIPTION = 'Jar archive'

    def __init__(self):
        super(Jar, self).__init__(
            extension=Jar.EXTENSION,
            mime=Jar.MIME,
            description=Jar.DESCRIPTION
        )

    def check(self, buf):
        return (len(buf) > 4 and
                buf[0] == 0x5F and
                buf[1] == 0x27 and
                buf[2] == 0xA8 and
                buf[3] == 0x89)



class Tarz(Extension):
    EXTENSION = 'tar.z'
    MIME = 'application/gzip'
    DESCRIPTION = 'Compressed tape archive file'

    def __init__(self):
        super(Tarz, self).__init__(
            extension=Tarz.EXTENSION,
            mime=Tarz.MIME,
            description=Tarz.DESCRIPTION
        )

    def check(self, buf):
        return (len(buf) > 2 and
                (buf[0] == 0x1F and
                 buf[1] == 0x9D)
                or
                (buf[0] == 0x1F and
                 buf[1] == 0xA0))



class Tarbz2(Extension):
    EXTENSION = 'tar.bz2'
    MIME = 'application/gzip'
    DESCRIPTION = 'bzip2 compressed archive'

    def __init__(self):
        super(Tarbz2, self).__init__(
            extension=Tarbz2.EXTENSION,
            mime=Tarbz2.MIME,
            description=Tarbz2.DESCRIPTION
        )

    def check(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x42 and
                buf[1] == 0x5A and
                buf[2] == 0x68)



class Tarxz(Extension):
    EXTENSION = 'tar.xz'
    MIME = 'application/gzip'
    DESCRIPTION = 'XZ compression utility using LZMA2 compression'

    def __init__(self):
        super(Tarxz, self).__init__(
            extension=Tarxz.EXTENSION,
            mime=Tarxz.MIME,
            description=Tarxz.DESCRIPTION
        )

    def check(self, buf):
        return (len(buf) > 7 and
                buf[0] == 0xFD and
                buf[1] == 0x37 and
                buf[2] == 0x7A and
                buf[3] == 0x58 and
                buf[4] == 0x5A and
                buf[5] == 0x00 and
                buf[6] == 0x00)


class Tar(Extension):
    EXTENSION = 'tar'
    MIME = 'application/x-tar'
    DESCRIPTION = 'tar archive'

    def __init__(self):
        super(Tar, self).__init__(
            extension=Tar.EXTENSION,
            mime=Tar.MIME,
            description=Tar.DESCRIPTION
        )

    def check(self, buf):
        return (len(buf) > 5 and
                buf[257] == 0x75 and
                buf[258] == 0x73 and
                buf[259] == 0x74 and
                buf[260] == 0x61 and
                buf[261] == 0x72)