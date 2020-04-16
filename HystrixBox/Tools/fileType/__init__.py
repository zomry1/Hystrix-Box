"""
This module is the Detect file type tool
Used in Ultimate Forensics Tool.

"""

from HystrixBox.Tools.fileType.applications import *
from HystrixBox.Tools.fileType.archives import *
from HystrixBox.Tools.fileType.audio import *
from HystrixBox.Tools.fileType.font import *
from HystrixBox.Tools.fileType.getFileExtenstion import getFileExtension, get_header
from HystrixBox.Tools.fileType.images import *
from HystrixBox.Tools.fileType.video import *

__all__ = ['Extension', 'getFileExtension', 'get_header',
           'Pcap', 'Pdf', 'Exe', 'Elf', 'Psd', 'Flash', 'Office',
           'Zip', 'Rar', 'Sevenz', 'Jar', 'Tarz', 'Tarbz2', 'Tarxz', 'Tar',
           'Wav', 'Aiff', 'Mp3', 'Aac', 'Mid', 'Flac', 'M4a', 'Ogg', 'Amr',
           'Otf', 'Ttf',
           'Jpeg', 'Png', 'Gif', 'Webp', 'Cr2', 'Tiff', 'Bmp', 'Fits', 'Ico',
           'Flv', 'Matroska', 'Avi', 'Mp4', 'Mov', 'Wmv']
