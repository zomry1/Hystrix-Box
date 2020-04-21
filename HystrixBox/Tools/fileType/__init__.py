"""
This module is the Detect file type tool
Used in Ultimate Forensics Tool.

"""

from Tools.fileType.applications import *
from Tools.fileType.archives import *
from Tools.fileType.audio import *
from Tools.fileType.font import *
from Tools.fileType.get_file_extension import get_file_extension, get_header
from Tools.fileType.images import *
from Tools.fileType.video import *

__all__ = ['Extension', 'get_file_extension', 'get_header',
           'Pcap', 'Pdf', 'Exe', 'Elf', 'Psd', 'Flash', 'Office',
           'Zip', 'Rar', 'Sevenz', 'Jar', 'Tarz', 'Tarbz2', 'Tarxz', 'Tar',
           'Wav', 'Aiff', 'Mp3', 'Aac', 'Mid', 'Flac', 'M4a', 'Ogg', 'Amr',
           'Otf', 'Ttf',
           'Jpeg', 'Png', 'Gif', 'Webp', 'Cr2', 'Tiff', 'Bmp', 'Fits', 'Ico',
           'Flv', 'Matroska', 'Avi', 'Mp4', 'Mov', 'Wmv']
