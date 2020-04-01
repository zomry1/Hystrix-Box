class Extension(object):
	def __init__(self, extensionName):
		self.__extensionName = extensionName

	@property
	def extensionName(self):
		return self.__extensionName

	# Check if the buf is indicate on this file type
	def check(self, buf):
		raise NotImplementedError
