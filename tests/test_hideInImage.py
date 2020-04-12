from Tools.hideInImage import findFiles
import filecmp

TEST1 = '''Hidden files extracted
File extension is: jpg\n'''
TEST2 = '''There is no hidden files in this image\n'''
TEST3 = '''File extension not found\n'''
TEST4 = '''Cant read the file\n'''
TEST5 = '''corrupted file\n'''
TEST6 = '''File extension is nor png or jpg\n'''
TEST7 = '''Hidden files extracted
File extension not found\n'''

def test_find_files_hiddenFileJpg(capfd, tmpdir):
    file = tmpdir.join('output')
    findFiles('../examples/HideInImage/hiddenInImage.jpg', file.strpath)
    out, err = capfd.readouterr()
    assert (filecmp.cmp(file.strpath + '.jpg', '../examples/HideInImage/hiddenFile.jpg')), 'Extracted files are not equals'
    assert (out == TEST1), 'stdout are not equals'


def test_find_files_noHidden(capfd, tmpdir):
    file = tmpdir.join('output')
    findFiles('../examples/strings.jpg', file.strpath)
    out, err = capfd.readouterr()
    assert (out == TEST2), 'stdout are not equals'


def test_find_files_noImage_txt(capfd, tmpdir):
    file = tmpdir.join('output')
    findFiles('../examples/extractor.txt', file.strpath)
    out, err = capfd.readouterr()
    assert (out == TEST3), 'stdout are not equals'


def test_find_files_noFile(capfd, tmpdir):
    file = tmpdir.join('outputt')
    findFiles('', file.strpath)
    out, err = capfd.readouterr()
    assert (out == TEST4), 'stdout are not equals'


def test_find_files_corruptedImageTrailer(capfd, tmpdir):
    file = tmpdir.join('output')
    findFiles('../examples/HideInImage/corruptedImageTrailer.jpg', file.strpath)
    out, err = capfd.readouterr()
    assert (out == TEST5), 'stdout are not equals'


def test_find_files_noImage_zip(capfd, tmpdir):
    file = tmpdir.join('output')
    findFiles('../examples/recursivezip.zip', file.strpath)
    out, err = capfd.readouterr()
    assert (out == TEST6), 'stdout are not equals'


def test_find_files_hiddenFilePng(capfd, tmpdir):
    file = tmpdir.join('output')
    findFiles('../examples/HideInImage/hiddenInImage.png', file.strpath)
    out, err = capfd.readouterr()
    assert (filecmp.cmp(file.strpath + '.jpg', '../examples/HideInImage/hiddenFile.jpg')), 'Extracted files are not equals'
    assert (out == TEST1), 'stdout are not equals'

def test_find_files_hiddenFileCorrupted(capfd, tmpdir):
    file = tmpdir.join('output')
    findFiles('../examples/HideInImage/hiddenInImageCorrupted.png', file.strpath)
    out, err = capfd.readouterr()
    assert (filecmp.cmp(file.strpath, '../examples/HideInImage/corruptedImage.jpg')), 'Extracted files are not equals'
    assert (out == TEST7), 'stdout are not equals'
