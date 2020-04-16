from HystrixBox.Tools.fileType.extenstion import Extension


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

    def check(self, header):
        return (len(header) > 4 and
                header[0] == 0x50 and
                header[1] == 0x4B and
                header[2] == 0x03 and
                header[3] == 0x04)


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

    def check(self, header):
        return (len(header) > 8 and  # first is v4 and the second is v5
                (header[0] == 0x52 and
                 header[1] == 0x61 and
                 header[2] == 0x72 and
                 header[3] == 0x21 and
                 header[4] == 0x1A and
                 header[5] == 0x07 and
                 header[6] == 0x00)
                or
                (header[0] == 0x52 and
                 header[1] == 0x61 and
                 header[2] == 0x72 and
                 header[3] == 0x21 and
                 header[4] == 0x1A and
                 header[5] == 0x07 and
                 header[6] == 0x01 and
                 header[7] == 0x00))


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

    def check(self, header):
        return (len(header) > 6 and
                header[0] == 0x37 and
                header[1] == 0x7A and
                header[2] == 0xBC and
                header[3] == 0xAF and
                header[4] == 0x27 and
                header[5] == 0x1C)



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

    def check(self, header):
        return (len(header) > 4 and
                header[0] == 0x5F and
                header[1] == 0x27 and
                header[2] == 0xA8 and
                header[3] == 0x89)



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

    def check(self, header):
        return (len(header) > 2 and
                (header[0] == 0x1F and
                 header[1] == 0x9D)
                or
                (header[0] == 0x1F and
                 header[1] == 0xA0))



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

    def check(self, header):
        return (len(header) > 3 and
                header[0] == 0x42 and
                header[1] == 0x5A and
                header[2] == 0x68)



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

    def check(self, header):
        return (len(header) > 7 and
                header[0] == 0xFD and
                header[1] == 0x37 and
                header[2] == 0x7A and
                header[3] == 0x58 and
                header[4] == 0x5A and
                header[5] == 0x00 and
                header[6] == 0x00)


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

    def check(self, header):
        return (len(header) > 5 and
                header[257] == 0x75 and
                header[258] == 0x73 and
                header[259] == 0x74 and
                header[260] == 0x61 and
                header[261] == 0x72)