import os
from pathlib import Path
import zipfile


def extract_recursive(filename, path=''):
    z = zipfile.ZipFile(filename)  # Open the zip file
    for f in z.namelist():  # Foreach file in the zip
        if f.endswith('.zip'):  # IF the file is a zip file
            dirname = os.path.splitext(f)[0]  # get directory name from file
            newPath = path + '/' + dirname
            Path(newPath).mkdir(exist_ok=True)
            z.extract(f, newPath)  # Extract the zip to the new directory
            extract_recursive(newPath + '/' + f, newPath)  # Recursively call this function with the new zip
            os.remove(newPath + '/' + f)  # Delete the temp zip file
        else: # It's a regular file
            z.extract(f, path) # Extract the file


# Run example
# extract_recursive('Tools/recursiveCheck/recursivezip.zip', 'recursiveCheck')
