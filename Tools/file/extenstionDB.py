import images
import applications

IMAGE_EXTENSIONS = [images.Jpeg(), images.Png(), images.Gif(), images.Webp(), images.Cr2(), images.Tiff(), images.Bmp(),
					images.Psd(), images.Fits(), images.Ico()]

APPLICATIONS_EXTENSTIONS = [applications.Pcap(), applications.Db(), applications.Pdf(), applications.Exe(), applications.Elf()]

EXTENSIONS = IMAGE_EXTENSIONS + APPLICATIONS_EXTENSTIONS
