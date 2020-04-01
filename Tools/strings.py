import string
from Utils.searchFlag import searchFlag


def strings(filename, minChars=4):
	with open(filename, errors="ignore") as f:
		result = ""
		for c in f.read():
			if c in string.printable:
				result += c
				continue
			if len(result) >= minChars:
				yield result
			result = ""
		if len(result) >= minChars:  # catch result at EOF
			yield result


def stringsFlag(filename, flagFormat, minChars=4):
	flags = []
	for text in strings(filename, minChars):
		flags += searchFlag(flagFormat, text)
	return flags