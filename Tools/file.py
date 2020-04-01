import filetype

#Need to install file type = pip install filetype

def fileExtension():
	kind = filetype.guess('me.txt')
	if kind is None:
		print('Cannot guess file type!')
		return

	print('File extension: %s' % kind.extension)
	print('File MIME type: %s' % kind.mime)


fileExtension()
