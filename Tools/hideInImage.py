from Tools.file.getFileExtenstion import getFileExtension
import os

def findFiles(filename, output='hiddenFile'):
    # Read image
    try:
        with open(filename, 'rb') as file:
            f = bytearray(file.read())
    except:
        print('Cant read the file')
        return

    endTag = 0
    # Check image format
    extension = getFileExtension(filename)
    if extension is None:
        print('File extension not found')
        return
    if extension.extension == 'jpg':
        endTag = bytearray(b'\xFF\xD9')
    elif extension.extension == 'png':
        endTag = bytearray(b'\x00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82')
    else:
        print('File extension is nor png or jpg')
        return

    # Find end png tag
    index = f.find(endTag)

    if index == -1:
        print('corrupted file')
        return

    if index+2 == len(f):
        print('There is no hidden files in this image')
        return

    # save all extra bytes to file
    with open(output, 'wb') as file:
        file.write(f[index + len(endTag):])
        print('Hidden files extracted')

    # Check with file command to detect file extension
    extension = getFileExtension(output)
    if extension is None:
        print('File extension not found')
        return
    print('File extension is: ' + extension.extension)

    '''
    # save file with correspond extension
    os.remove(output)
    with open(output + '.' + extension.extension, 'wb') as file:
        file.write(f[index + len(endTag):])
        print('Hidden files extracted')
    '''

