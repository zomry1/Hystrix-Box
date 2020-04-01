class Extension(object):
	def __init__(self, extension, mime,  description):
		self.__extension = extension
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

	# Check if the buf is indicate on this file type
	def check(self, buf):
		raise NotImplementedError

	def __str__(self):
		return 'File extension: ' + self.__extension + '\nMIME: ' + self.__mime + '\ndescription: ' + self.__description
