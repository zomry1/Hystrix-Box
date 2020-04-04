from extenstionDB import EXTENSIONS
import time

HEADER_BYTES = 262


# Add this function to add decorator of @timing to measure function runtime
def timing(f):
	def wrap(*args):
		time1 = time.time()
		for i in range(2000):
			ret = f(*args)
		time2 = time.time()
		print('{:s} function took {:.3f} ms'.format(f.__name__, (time2 - time1) / 2))
		return ret

	return wrap


def get_header(filePath):
	# Need to add checking for file with zero lenght
	try:
		with open(filePath, 'rb') as file:
			return bytearray(file.read(HEADER_BYTES))
	except:
		print('Cant read the file')
		return None


@timing
def getFileExtension(filePath):
	header = get_header(filePath)
	if not header:
		exit()

	for extension in EXTENSIONS:
		if extension.check(header):
			return extension
	return None


print(getFileExtension("Examples/WAV.wav"))
