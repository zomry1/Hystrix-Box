from Tools.recursiveDecompression import extract_recursive
import filecmp
import os

TEST1 = '''File not found\n'''
TEST2 = '''Not a zip file or corrupted zip file\n'''


def compareDir(dir1, dir2):
    """
        Compare two directory trees content.
        Return False if they differ, True is they are the same.
        """
    compared = filecmp.dircmp(dir1, dir2)
    if (compared.left_only or compared.right_only or compared.diff_files
            or compared.funny_files):
        return False
    for subdir in compared.common_dirs:
        if not compareDir(os.path.join(dir1, subdir), os.path.join(dir2, subdir)):
            return False
    return True


def test_extract_recursive_true(tmpdir):
    path = tmpdir.strpath
    extract_recursive('../examples/recursivezip.zip', path)
    assert compareDir(path, '../examples/RecursiveZipExtracted/')


def test_extract_recursive_1layer(tmpdir):
    path = tmpdir.strpath
    extract_recursive('../examples/root.zip', path)
    assert compareDir(path, '../examples/RecursiveZipExtracted/1Introduction/2Introduction/3Introduction')


def test_extract_recursive_noFile(capfd, tmpdir):
    path = tmpdir.strpath
    extract_recursive('', path)
    out, err = capfd.readouterr()
    assert (out == TEST1)


def test_extract_recursive_noZipFile(capfd, tmpdir):
    path = tmpdir.strpath
    extract_recursive('../examples/extractor.txt', path)
    out, err = capfd.readouterr()
    assert (out == TEST2)
