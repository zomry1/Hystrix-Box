from extenstion import Extension


class Jpeg(Extension):
	EXTENSION = 'jpg'

	def __init__(self):
		super(Jpeg, self).__init__(
			extensionName=Jpeg.EXTENSION
		)

	def check(self, buf):
		return (len(buf) > 2 and
				buf[0] == 0xFF and
				buf[1] == 0xD8 and
				buf[2] == 0xFF)


class Png(Extension):
	EXTENSION = 'png'

	def __init__(self):
		super(Png, self).__init__(
			extensionName=Png.EXTENSION
		)

	def check(self, buf):
		return (len(buf) > 3 and
				buf[0] == 0x89 and
				buf[1] == 0x50 and
				buf[2] == 0x4E and
				buf[3] == 0x47)


class Gif(Extension):
	EXTENSION = 'gif'

	def __init__(self):
		super(Gif, self).__init__(
			extensionName=Gif.EXTENSION
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
