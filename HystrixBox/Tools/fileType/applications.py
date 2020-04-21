from Tools.fileType.extenstion import Extension


# https://www.iana.org/assignments/media-types/application/vnd.tcpdump.pcap
class Pcap(Extension):
    EXTENSION = 'pcap'  # Can also be cap and dmp
    MIME = 'application/vnd.tcpdump.pcap'
    DESCRIPTION = 'tcpdump (libpcap) capture file'
    OTHER_EXTENSIONS = 'cap, dmp'

    def __init__(self):
        super(Pcap, self).__init__(
            extension=Pcap.EXTENSION,
            mime=Pcap.MIME,
            description=Pcap.DESCRIPTION,
            otherExtensions=Pcap.OTHER_EXTENSIONS
        )

    def check(self, header):
        return (len(header) > 4 and
                (header[0] == 0xA1 and
                 header[1] == 0xB2 and
                 header[2] == 0xC3 and
                 header[3] == 0xD4)
                or
                (header[0] == 0xD4 and
                 header[1] == 0xC3 and
                 header[2] == 0xB2 and
                 header[3] == 0xA1)
                )


# https://www.iana.org/assignments/media-types/application/vnd.sqlite3
class Db(Extension):
    EXTENSION = 'db'
    MIME = 'application/vnd.sqlite3'
    DESCRIPTION = 'SQLite database file'
    OTHER_EXTENSIONS = 'sqllitedb, sqlite'

    def __init__(self):
        super(Db, self).__init__(
            extension=Db.EXTENSION,
            mime=Db.MIME,
            description=Db.DESCRIPTION,
            otherExtensions=Db.OTHER_EXTENSIONS
        )

    def check(self, header):
        return (len(header) > 16 and
                header[0] == 0x53 and
                header[1] == 0x51 and
                header[2] == 0x4C and
                header[3] == 0x69 and
                header[4] == 0x74 and
                header[5] == 0x65 and
                header[6] == 0x20 and
                header[7] == 0x66 and
                header[8] == 0x6F and
                header[9] == 0x72 and
                header[10] == 0x6D and
                header[11] == 0x61 and
                header[12] == 0x74 and
                header[13] == 0x20 and
                header[14] == 0x33 and
                header[15] == 0x00)


# https://tools.ietf.org/html/rfc8118
class Pdf(Extension):  # Print version = print(buf[5:8])
    EXTENSION = 'pdf'
    MIME = 'application/pdf'
    DESCRIPTION = 'Adobe Portable Document Format'

    def __init__(self):
        super(Pdf, self).__init__(
            extension=Pdf.EXTENSION,
            mime=Pdf.MIME,
            description=Pdf.DESCRIPTION
        )

    def check(self, header):
        return (len(header) > 5 and
                header[0] == 0x25 and
                header[1] == 0x50 and
                header[2] == 0x44 and
                header[3] == 0x46 and
                header[4] == 0x2D)


# https://www.iana.org/assignments/media-types/application/vnd.microsoft.portable-executable
class Exe(Extension):
    EXTENSION = 'exe'
    MIME = 'application/vnd.microsoft.portable-executable'
    DESCRIPTION = 'Windows/DOS executable file'
    OTHER_EXTENSIONS = 'dll'

    def __init__(self):
        super(Exe, self).__init__(
            extension=Exe.EXTENSION,
            mime=Exe.MIME,
            description=Exe.DESCRIPTION,
            otherExtensions=Exe.OTHER_EXTENSIONS
        )

    def check(self, header):
        return (len(header) > 2 and
                header[0] == 0x4D and
                header[1] == 0x5A)


# https://www.iana.org/assignments/media-types/application/vnd.microsoft.portable-executable
class Elf(Extension):
    EXTENSION = 'elf'
    MIME = 'application/x-elf'
    DESCRIPTION = 'Executable and Linkable Format'

    def __init__(self):
        super(Elf, self).__init__(
            extension=Elf.EXTENSION,
            mime=Elf.MIME,
            description=Elf.DESCRIPTION
        )

    def check(self, header):
        return (len(header) > 4 and
                header[0] == 0x7F and
                header[1] == 0x45 and
                header[2] == 0x4C and
                header[3] == 0x46)


# https://www.iana.org/assignments/media-types/image/vnd.adobe.photoshop
class Psd(Extension):
    EXTENSION = 'psd'
    MIME = 'application/vnd.adobe.photoshop'
    DESCRIPTION = 'Photoshop image file'

    def __init__(self):
        super(Psd, self).__init__(
            extension=Psd.EXTENSION,
            mime=Psd.MIME,
            description=Psd.DESCRIPTION
        )

    def check(self, header):
        return (len(header) > 4 and
                header[0] == 0x38 and
                header[1] == 0x42 and
                header[2] == 0x50 and
                header[3] == 0x53)


# https://www.iana.org/assignments/media-types/image/vnd.adobe.photoshop
class Flash(Extension):
    EXTENSION = 'swf'
    MIME = 'application/vnd.adobe.flash.movie'
    DESCRIPTION = 'Macromedia Shockwave Flash player file'

    def __init__(self):
        super(Flash, self).__init__(
            extension=Flash.EXTENSION,
            mime=Flash.MIME,
            description=Flash.DESCRIPTION
        )

    def check(self, header):
        return (len(header) > 3 and
                (header[0] == 0x5A and
                 header[1] == 0x57 and
                 header[2] == 0x53)
                or
                (header[0] == 0x43 and
                 header[1] == 0x57 and
                 header[2] == 0x53))


class Office(Extension):
    EXTENSION = 'doc'
    MIME = 'application/vnd.ms'
    DESCRIPTION = 'An Object Linking and Embedding (OLE) Compound File (CF)'
    OTHER_EXTENSIONS = 'xls, vsd, ppt, msi, msg'

    def __init__(self):
        super(Office, self).__init__(
            extension=Office.EXTENSION,
            mime=Office.MIME,
            description=Office.DESCRIPTION,
            otherExtensions=Office.OTHER_EXTENSIONS
        )

    def check(self, header):
        return (len(header) > 8 and
                header[0] == 0xD0 and
                header[1] == 0xCF and
                header[2] == 0x11 and
                header[3] == 0xE0 and
                header[4] == 0xA1 and
                header[5] == 0xB1 and
                header[6] == 0x1A and
                header[7] == 0xE1)
