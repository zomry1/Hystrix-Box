from HystrixBox.Tools.fileType.get_file_extension import get_file_extension

TEST1 = '''Cant read the file\n'''


def test_get_file_extension_nofile(capfd):
    extension = get_file_extension('')
    out, err = capfd.readouterr()
    assert (extension is None and out == TEST1)


def test_get_file_extension_bmp_all():
    extension = get_file_extension('../examples/DetectFileFormat/BMP.BMP')
    assert (
            extension.extension == 'bmp' and
            extension.mime == 'image/bmp' and
            extension.description == 'Windows (or device-independent) bitmap image' and
            str(extension) ==
            'File extension: bmp\nother extensions names: \nMIME: image/bmp\ndescription: Windows (or '
            'device-independent) bitmap image')


def test_get_file_extension_bmp():
    assert (get_file_extension('../examples/DetectFileFormat/BMP.BMP').extension == 'bmp')


def test_get_file_extension_cr2():
    assert (get_file_extension('../examples/DetectFileFormat/CR2.CR2').extension == 'cr2')


def test_get_file_extension_db():
    assert (get_file_extension('../examples/DetectFileFormat/DB.db').extension == 'db')


def test_get_file_extension_elf():
    assert (get_file_extension('../examples/DetectFileFormat/ELF.elf').extension == 'elf')


def test_get_file_extension_exe():
    assert (get_file_extension('../examples/DetectFileFormat/EXE.exe').extension == 'exe')


def test_get_file_extension_fits():
    assert (get_file_extension('../examples/DetectFileFormat/FITS.fits').extension == 'fits')


def test_get_file_extension_gif():
    assert (get_file_extension('../examples/DetectFileFormat/GIF.gif').extension == 'gif')


def test_get_file_extension_ico():
    assert (get_file_extension('../examples/DetectFileFormat/ICO.ico').extension == 'ico')


def test_get_file_extension_jpeg():
    assert (get_file_extension('../examples/DetectFileFormat/JPEG.jpg').extension == 'jpg')


def test_get_file_extension_mp4():
    assert (get_file_extension('../examples/DetectFileFormat/MP4.mp4').extension == 'mp4')


def test_get_file_extension_pcap():
    assert (get_file_extension('../examples/DetectFileFormat/PCAP.pcap').extension == 'pcap')


def test_get_file_extension_pdf():
    assert (get_file_extension('../examples/DetectFileFormat/PDF.pdf').extension == 'pdf')


def test_get_file_extension_png():
    assert (get_file_extension('../examples/DetectFileFormat/PNG.png').extension == 'png')


def test_get_file_extension_psd():
    assert (get_file_extension('../examples/DetectFileFormat/PSD.psd').extension == 'psd')


def test_get_file_extension_tar():
    assert (get_file_extension('../examples/DetectFileFormat/TAR.tar').extension == 'tar')


def test_get_file_extension_tif():
    assert (get_file_extension('../examples/DetectFileFormat/TIF.TIF').extension == 'tif')


def test_get_file_extension_wav():
    assert (get_file_extension('../examples/DetectFileFormat/WAV.wav').extension == 'wav')


def test_get_file_extension_webp():
    assert (get_file_extension('../examples/DetectFileFormat/WEBP.webp').extension == 'webp')


def test_get_file_extension_zip():
    assert (get_file_extension('../examples/DetectFileFormat/ZIP.zip').extension == 'zip')
