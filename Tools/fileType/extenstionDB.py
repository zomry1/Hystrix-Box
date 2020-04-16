from Tools.fileType import images, applications, audio, archives, font, video

IMAGE_EXTENSIONS = [images.Jpeg(), images.Png(), images.Gif(), images.Webp(), images.Cr2(), images.Tiff(), images.Bmp(),
                    images.Fits(), images.Ico()]

APPLICATIONS_EXTENSIONS = [applications.Pcap(), applications.Db(), applications.Pdf(), applications.Exe(),
                           applications.Elf(), applications.Psd(), applications.Flash(), applications.Office()]

AUDIO_EXTENSIONS = [audio.Wav(), audio.Aiff(), audio.Mp3(), audio.Aac(), audio.Mid(), audio.Flac(), audio.M4a(),
                    audio.Ogg(), audio.Amr()]

ARCHIVE_EXTENSIONS = [archives.Zip(), archives.Rar(), archives.Sevenz(), archives.Jar(), archives.Tarz(),
                      archives.Tarbz2(), archives.Tarxz(), archives.Tar()]

VIDEO_EXTENSIONS = [video.Avi(), video.Flv(), video.Matroska(), video.Mov(), video.Mp4(), video.Wmv()]

FONTS_EXTENSIONS = [font.Otf(), font.Ttf()]

ALL_EXTENSIONS = IMAGE_EXTENSIONS + APPLICATIONS_EXTENSIONS + AUDIO_EXTENSIONS + ARCHIVE_EXTENSIONS + FONTS_EXTENSIONS \
                 + VIDEO_EXTENSIONS
