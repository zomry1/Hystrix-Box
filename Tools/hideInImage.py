def findFiles(filename):
    # Read image
    try:
        with open(filename, 'rb') as file:
            f = bytearray(file.read())
    except:
        print('Cant read the file')
        return

    # Find end jpg tag
    index = f.rfind(0xFF, 0xD9)
    if index == -1:
        print('Not jpg file or corrupted file')
        return

    if index+2 == len(f):
        print('There is no hidden files in this image')
        return

    # save all extra bytes to file
    with open('hiddenFile', 'wb') as file:
        file.write(f[index + 2:])
        print('Hidden files extracted')

    # Check with file command to check if it's a file



findFiles("me.txt") #Text file
findFiles("JPEG.jpg") #Regular jpg file
findFiles("hideInImage.jpg") #Jpg file with hidden files
