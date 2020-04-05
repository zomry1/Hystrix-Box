from Tools.file import images, applications, audio, archives

IMAGE_EXTENSIONS = [images.Jpeg(), images.Png(), images.Gif(), images.Webp(), images.Cr2(), images.Tiff(), images.Bmp(),
                    images.Psd(), images.Fits(), images.Ico()]

APPLICATIONS_EXTENSIONS = [applications.Pcap(), applications.Db(), applications.Pdf(), applications.Exe(),
                            applications.Elf()]

AUDIO_EXTENSIONS = [audio.Wav(), audio.Aiff(), audio.Mp3(), audio.Aac(), audio.Mid(), audio.Flac(), audio.M4a(),
                    audio.Ogg(), audio.Amr()]

ARCHIVE_EXTENSIONS = [archives.Zip()]

EXTENSIONS = IMAGE_EXTENSIONS + APPLICATIONS_EXTENSIONS + AUDIO_EXTENSIONS + ARCHIVE_EXTENSIONS
