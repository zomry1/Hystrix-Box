class Extension(object):
	def __init__(self, extension, mime, description, otherExtensions=''):
		self.__extension = extension
		self._otherExtensions = otherExtensions
		self.__mime = mime
		self.__description = description

	@property
	def extension(self):
		return self.__extension

	@property
	def mime(self):
		return self.__mime

	@property
	def description(self):
		return self.__description

	# Check if the magic numbers are in the header
	def check(self, header):
		raise NotImplementedError

	def __str__(self):
		return 'File extension: ' + self.__extension + '\nother extensions names: ' + self._otherExtensions + '\nMIME: ' + self.__mime + '\ndescription: ' + self.__description
