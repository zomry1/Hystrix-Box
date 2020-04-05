from Tools.file.getFileExtenstion import getFileExtension


def findFiles(filename, output='hiddenFile'):
    # Read image
    try:
        with open(filename, 'rb') as file:
            f = bytearray(file.read())
    except:
        print('Cant read the file')
        return

    # Find end jpg tag
    index = f.find(0xFF, 0xD9)
    if index == -1:
        print('Not jpg file or corrupted file')
        return

    if index+2 == len(f):
        print('There is no hidden files in this image')
        return

    # save all extra bytes to file
    with open(output, 'wb') as file:
        file.write(f[index + 2:])
        print('Hidden files extracted')

    # Check with file command to detect file extension
    extension = getFileExtension(output)
    if extension is None:
        print('File extension not found')
    print('File extension is: ' + extension.extension)

    # save all extra bytes to file
    with open(output + extension.extension, 'wb') as file:
        file.write(f[index + 2:])
        print('Hidden files extracted')



#findFiles("me.txt") #Text file
#findFiles("JPEG.jpg") #Regular jpg file
#findFiles("hideInImage.jpg") #Jpg file with hidden files
findFiles('hiddenCheck/hideInImage.jpg')
