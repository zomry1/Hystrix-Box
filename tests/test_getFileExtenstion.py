from Tools.file.getFileExtenstion import getFileExtension

TEST1 = '''Cant read the file\n'''


def test_get_file_extension_nofile(capfd):
    extension = getFileExtension('')
    out, err = capfd.readouterr()
    assert (extension is None and out == TEST1)


def test_get_file_extension_bmp():
    extension = getFileExtension('../examples/DetectFileFormat/BMP.BMP')
    assert (
            extension.extension == 'bmp' and extension.mime == 'image/bmp' and extension.description == 'Windows (or '
                                                                                                        'device'
                                                                                                        '-independent'
                                                                                                        ') bitmap '
                                                                                                        'image '
            and str(extension) ==
            'File extension: bmp\nother extensions names: \nMIME: image/bmp\ndescription: Windows (or '
            'device-independent) bitmap image')


def test_get_file_extension_bmp():
    assert (getFileExtension('../examples/DetectFileFormat/BMP.BMP').extension == 'bmp')


def test_get_file_extension_cr2():
    assert (getFileExtension('../examples/DetectFileFormat/CR2.CR2').extension == 'cr2')


def test_get_file_extension_db():
    assert (getFileExtension('../examples/DetectFileFormat/DB.db').extension == 'db')


def test_get_file_extension_elf():
    assert (getFileExtension('../examples/DetectFileFormat/ELF.elf').extension == 'elf')


def test_get_file_extension_exe():
    assert (getFileExtension('../examples/DetectFileFormat/EXE.exe').extension == 'exe')


def test_get_file_extension_fits():
    assert (getFileExtension('../examples/DetectFileFormat/FITS.fits').extension == 'fits')


def test_get_file_extension_gif():
    assert (getFileExtension('../examples/DetectFileFormat/GIF.gif').extension == 'gif')


def test_get_file_extension_ico():
    assert (getFileExtension('../examples/DetectFileFormat/ICO.ico').extension == 'ico')


def test_get_file_extension_jpeg():
    assert (getFileExtension('../examples/DetectFileFormat/JPEG.jpg').extension == 'jpg')


def test_get_file_extension_mp4():
    assert (getFileExtension('../examples/DetectFileFormat/MP4.mp4').extension == 'mp4')


def test_get_file_extension_pcap():
    assert (getFileExtension('../examples/DetectFileFormat/PCAP.pcap').extension == 'pcap')


def test_get_file_extension_pdf():
    assert (getFileExtension('../examples/DetectFileFormat/PDF.pdf').extension == 'pdf')


def test_get_file_extension_png():
    assert (getFileExtension('../examples/DetectFileFormat/PNG.png').extension == 'png')


def test_get_file_extension_psd():
    assert (getFileExtension('../examples/DetectFileFormat/PSD.psd').extension == 'psd')


def test_get_file_extension_tar():
    assert (getFileExtension('../examples/DetectFileFormat/TAR.tar').extension == 'tar')


def test_get_file_extension_tif():
    assert (getFileExtension('../examples/DetectFileFormat/TIF.TIF').extension == 'tif')


def test_get_file_extension_wav():
    assert (getFileExtension('../examples/DetectFileFormat/WAV.wav').extension == 'wav')


def test_get_file_extension_webp():
    assert (getFileExtension('../examples/DetectFileFormat/WEBP.webp').extension == 'webp')


def test_get_file_extension_zip():
    assert (getFileExtension('../examples/DetectFileFormat/ZIP.zip').extension == 'zip')
