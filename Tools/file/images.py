from Tools.file.extenstion import Extension

class Jpeg(Extension):
	EXTENSION = 'jpg'
	MIME = 'image/jpeg'
	DESCRIPTION = 'Generic JPEGimage file'

	def __init__(self):
		super(Jpeg, self).__init__(
			extension=Jpeg.EXTENSION,
			mime=Jpeg.MIME,
			description=Jpeg.DESCRIPTION
		)

	def check(self, buf):
		return (len(buf) > 2 and
				buf[0] == 0xFF and
				buf[1] == 0xD8 and
				buf[2] == 0xFF)


class Png(Extension):
	EXTENSION = 'png'
	MIME = 'image/png'
	DESCRIPTION = 'Portable Network Graphics file'

	def __init__(self):
		super(Png, self).__init__(
			extension=Png.EXTENSION,
			mime=Png.MIME,
			description=Png.DESCRIPTION
		)

	def check(self, buf):
		return (len(buf) > 3 and
				buf[0] == 0x89 and
				buf[1] == 0x50 and
				buf[2] == 0x4E and
				buf[3] == 0x47)


class Gif(Extension):
	EXTENSION = 'gif'
	MIME = 'image/gif'
	DESCRIPTION = 'Graphics interchange format file'

	def __init__(self):
		super(Gif, self).__init__(
			extension=Gif.EXTENSION,
			mime=Gif.MIME,
			description=Gif.DESCRIPTION
		)

	def check(self, buf):
		return (len(buf) > 6 and
				(buf[0] == 0x47 and
				 buf[1] == 0x49 and
				 buf[2] == 0x46 and
				 buf[3] == 0x38 and
				 buf[4] == 0x37 and
				 buf[5] == 0x61)
				or
				(buf[0] == 0x47 and
				 buf[1] == 0x49 and
				 buf[2] == 0x46 and
				 buf[3] == 0x38 and
				 buf[4] == 0x39 and
				 buf[5] == 0x61))


class Webp(Extension):
	EXTENSION = 'webp'
	MIME = 'image/webp'
	DESCRIPTION = 'Google WebP image file'

	def __init__(self):
		super(Webp, self).__init__(
			extension=Webp.EXTENSION,
			mime=Webp.MIME,
			description=Webp.DESCRIPTION
		)

	def check(self, buf):  # Add checking for file size in bytes 4-7
		return (len(buf) > 12 and
				buf[0] == 0x52 and
				buf[1] == 0x49 and
				buf[2] == 0x46 and
				buf[3] == 0x46 and
				buf[8] == 0x57 and
				buf[9] == 0x45 and
				buf[10] == 0x42 and
				buf[11] == 0x50)


class Cr2(Extension):
	EXTENSION = 'cr2'
	MIME = 'image/x-canon-cr2'
	DESCRIPTION = 'Canon digital camera RAW file'

	def __init__(self):
		super(Cr2, self).__init__(
			extension=Cr2.EXTENSION,
			mime=Cr2.MIME,
			description=Cr2.DESCRIPTION
		)

	def check(self, buf):  # Add checking for file size in bytes 4-7
		return (len(buf) > 10 and
				buf[0] == 0x49 and
				buf[1] == 0x49 and
				buf[2] == 0x2A and
				buf[3] == 0x00 and
				buf[4] == 0x10 and
				buf[5] == 0x00 and
				buf[6] == 0x00 and
				buf[7] == 0x00 and
				buf[8] == 0x43 and
				buf[9] == 0x52)


class Tiff(Extension):
	EXTENSION = 'tif'
	MIME = 'image/tiff'
	DESCRIPTION = 'Tagged Image File Format file'

	def __init__(self):
		super(Tiff, self).__init__(
			extension=Tiff.EXTENSION,
			mime=Tiff.MIME,
			description=Tiff.DESCRIPTION
		)

	def check(self, buf):
		return (len(buf) > 3 and
				(buf[0] == 0x49 and
				 buf[1] == 0x20 and
				 buf[2] == 0x49)
				or
				(buf[0] == 0x49 and
				 buf[1] == 0x49 and
				 buf[2] == 0x2A and
				 buf[3] == 0x00)
				or
				(buf[0] == 0x4D and
				 buf[1] == 0x4D and
				 buf[2] == 0x00 and
				 buf[3] == 0x2A)
				or
				(buf[0] == 0x4D and
				 buf[1] == 0x4D and
				 buf[2] == 0x00 and
				 buf[3] == 0x2B)
				)


# https://tools.ietf.org/html/rfc7903
class Bmp(Extension):
	EXTENSION = 'bmp'
	MIME = 'image/bmp'
	DESCRIPTION = 'Windows (or device-independent) bitmap image'

	def __init__(self):
		super(Bmp, self).__init__(
			extension=Bmp.EXTENSION,
			mime=Bmp.MIME,
			description=Bmp.DESCRIPTION
		)

	def check(self, buf):  # Bytes 2-5 are for file lenght in little endian
		return (len(buf) > 2 and
				buf[0] == 0x42 and
				buf[1] == 0x4D)


# https://www.iana.org/assignments/media-types/image/vnd.adobe.photoshop
class Psd(Extension):
	EXTENSION = 'psd'
	MIME = 'image/vnd.adobe.photoshop'
	DESCRIPTION = 'Photoshop image file'

	def __init__(self):
		super(Psd, self).__init__(
			extension=Psd.EXTENSION,
			mime=Psd.MIME,
			description=Psd.DESCRIPTION
		)

	def check(self, buf):
		return (len(buf) > 4 and
				buf[0] == 0x38 and
				buf[1] == 0x42 and
				buf[2] == 0x50 and
				buf[3] == 0x53)


# https://tools.ietf.org/html/rfc4047
class Fits(Extension):
	EXTENSION = 'fits'
	MIME = 'image/fits'
	DESCRIPTION = 'Flexible Image Transport System (FITS), Version 3.0 file'

	def __init__(self):
		super(Fits, self).__init__(
			extension=Fits.EXTENSION,
			mime=Fits.MIME,
			description=Fits.DESCRIPTION
		)

	def check(self, buf):
		return (len(buf) > 30 and
				buf[0] == 0x53 and
				buf[1] == 0x49 and
				buf[2] == 0x4D and
				buf[3] == 0x50 and
				buf[4] == 0x4C and
				buf[5] == 0x45 and
				buf[6] == 0x20 and
				buf[7] == 0x20 and
				buf[8] == 0x3D and
				buf[9] == 0x20 and
				buf[10] == 0x20 and
				buf[11] == 0x20 and
				buf[12] == 0x20 and
				buf[13] == 0x20 and
				buf[14] == 0x20 and
				buf[15] == 0x20 and
				buf[16] == 0x20 and
				buf[17] == 0x20 and
				buf[18] == 0x20 and
				buf[19] == 0x20 and
				buf[20] == 0x20 and
				buf[21] == 0x20 and
				buf[22] == 0x20 and
				buf[23] == 0x20 and
				buf[24] == 0x20 and
				buf[25] == 0x20 and
				buf[26] == 0x20 and
				buf[27] == 0x20 and
				buf[28] == 0x20 and
				buf[29] == 0x54)


# https://www.iana.org/assignments/media-types/image/vnd.microsoft.icon
class Ico(Extension):
	EXTENSION = 'ico'
	MIME = 'image/vnd.microsoft.icon'
	DESCRIPTION = 'Windows icon file'

	def __init__(self):
		super(Ico, self).__init__(
			extension=Ico.EXTENSION,
			mime=Ico.MIME,
			description=Ico.DESCRIPTION
		)

	def check(self, buf):
		return (len(buf) > 4 and
				buf[0] == 0x00 and
				buf[1] == 0x00 and
				buf[2] == 0x01 and
				buf[3] == 0x00)