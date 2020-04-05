from Tools.file.extenstion import Extension

# https://www.iana.org/assignments/media-types/application/vnd.tcpdump.pcap
class Pcap(Extension):
	EXTENSION = 'pcap (cap, dmp)' # Can also be cap and dmp
	MIME = 'application/vnd.tcpdump.pcap'
	DESCRIPTION = 'tcpdump (libpcap) capture file'

	def __init__(self):
		super(Pcap, self).__init__(
			extension=Pcap.EXTENSION,
			mime=Pcap.MIME,
			description=Pcap.DESCRIPTION
		)

	def check(self, buf):
		return (len(buf) > 4 and
				(buf[0] == 0xA1 and
				buf[1] == 0xB2 and
				buf[2] == 0xC3 and
				buf[3] == 0XD4)
				or
				(buf[0] == 0xD4 and
				buf[1] == 0xC3 and
				buf[2] == 0xB2 and
				buf[3] == 0xA1)
				)



# https://www.iana.org/assignments/media-types/application/vnd.sqlite3
class Db(Extension):
	EXTENSION = 'db (sqllitedb, sqlite)'
	MIME = 'application/vnd.sqlite3'
	DESCRIPTION = 'SQLite database file'

	def __init__(self):
		super(Db, self).__init__(
			extension=Db.EXTENSION,
			mime=Db.MIME,
			description=Db.DESCRIPTION
		)

	def check(self, buf):
		return (len(buf) > 16 and
				buf[0] == 0x53 and
				buf[1] == 0x51 and
				buf[2] == 0x4C and
				buf[3] == 0X69 and
				buf[4] == 0x74 and
				buf[5] == 0x65 and
				buf[6] == 0x20 and
				buf[7] == 0x66 and
				buf[8] == 0x6F and
				buf[9] == 0x72 and
				buf[10] == 0x6D and
				buf[11] == 0X61 and
				buf[12] == 0x74 and
				buf[13] == 0x20 and
				buf[14] == 0x33 and
				buf[15] == 0x00)


# https://tools.ietf.org/html/rfc8118
class Pdf(Extension): # Print version = print(buf[5:8])
	EXTENSION = 'pdf'
	MIME = 'application/pdf'
	DESCRIPTION = 'Adobe Portable Document Format'

	def __init__(self):
		super(Pdf, self).__init__(
			extension=Pdf.EXTENSION,
			mime=Pdf.MIME,
			description=Pdf.DESCRIPTION
		)

	def check(self, buf):
		return (len(buf) > 5 and
				buf[0] == 0x25 and
				buf[1] == 0x50 and
				buf[2] == 0x44 and
				buf[3] == 0X46 and
				buf[4] == 0x2D)


# https://www.iana.org/assignments/media-types/application/vnd.microsoft.portable-executable
class Exe(Extension):
	EXTENSION = 'exe (dll)'
	MIME = 'application/vnd.microsoft.portable-executable'
	DESCRIPTION = 'Windows/DOS executable file'

	def __init__(self):
		super(Exe, self).__init__(
			extension=Exe.EXTENSION,
			mime=Exe.MIME,
			description=Exe.DESCRIPTION
		)

	def check(self, buf):
		return (len(buf) > 2 and
				buf[0] == 0x4D and
				buf[1] == 0x5A)

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

	def check(self, buf):
		return (len(buf) > 4 and
				buf[0] == 0x7F and
				buf[1] == 0x45 and
				buf[2] == 0x4C and
				buf[3] == 0x46)
