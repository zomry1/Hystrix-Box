from Tools.file.extenstion import Extension


class Wav(Extension):
    EXTENSION = 'wav'
    MIME = 'audio/wav'
    DESCRIPTION = 'Waveform Audio File Format'

    def __init__(self):
        super(Wav, self).__init__(
            extension=Wav.EXTENSION,
            mime=Wav.MIME,
            description=Wav.DESCRIPTION
        )

    @staticmethod
    def check(buf): #Add size checking in bytes 5-8 (little endian)
        return (len(buf) > 16 and
                buf[0] == 0x52 and
                buf[1] == 0x49 and
                buf[2] == 0x46 and
                buf[3] == 0x46 and
                buf[8] == 0x57 and
                buf[9] == 0x41 and
                buf[10] == 0x56 and
                buf[11] == 0x45 and
                buf[12] == 0x66 and
                buf[13] == 0x6D and
                buf[14] == 0x74 and
                buf[15] == 0x20)


class Aiff(Extension):
    EXTENSION = 'aiff (aif, aifc)'
    MIME = 'audio/aiff'
    DESCRIPTION = 'Audio Interchange File Format'

    def __init__(self):
        super(Aiff, self).__init__(
            extension=Aiff.EXTENSION,
            mime=Aiff.MIME,
            description=Aiff.DESCRIPTION
        )

    @staticmethod
    def check(buf):
        return (len(buf) > 5 and
                buf[0] == 0x46 and
                buf[1] == 0x4F and
                buf[2] == 0x52 and
                buf[3] == 0x4D and
                buf[8] == 0x00)


class Mp3(Extension):
    EXTENSION = 'mp3'
    MIME = 'audio/mpeg'
    DESCRIPTION = 'MPEG-1 Audio Layer 3 (MP3) audio file'

    def __init__(self):
        super(Mp3, self).__init__(
            extension=Mp3.EXTENSION,
            mime=Mp3.MIME,
            description=Mp3.DESCRIPTION
        )

    @staticmethod
    def check(buf):
        return (len(buf) > 3 and
                buf[0] == 0x49 and
                buf[1] == 0x44 and
                buf[2] == 0x33)


class Aac(Extension):
    EXTENSION = 'aac'
    MIME = 'audio/aac'
    DESCRIPTION = 'Advanced Audio Coding (AAC) Low Complexity (LC) audio file'

    def __init__(self):
        super(Aac, self).__init__(
            extension=Aac.EXTENSION,
            mime=Aac.MIME,
            description=Aac.DESCRIPTION
        )

    @staticmethod
    def check(buf):
        return (len(buf) > 3 and
                (buf[0] == 0xFF and
                 buf[1] == 0xF1)
                or
                (buf[0] == 0xFF and
                 buf[1] == 0xF9)
                )

class Mid(Extension):
    EXTENSION = 'mid (midi)'
    MIME = 'audio/midi'
    DESCRIPTION = 'Musical Instrument Digital Interface (MIDI) sound file'

    def __init__(self):
        super(Mid, self).__init__(
            extension=Mid.EXTENSION,
            mime=Mid.MIME,
            description=Mid.DESCRIPTION
        )

    @staticmethod
    def check(buf):
        return (len(buf) > 4 and
                buf[0] == 0x4D and
                buf[1] == 0x54 and
                buf[2] == 0x68 and
                buf[3] == 0x64)


class Flac(Extension):
    EXTENSION = 'flac'
    MIME = 'audio/flac'
    DESCRIPTION = 'Free Lossless Audio Codec file'

    def __init__(self):
        super(Flac, self).__init__(
            extension=Flac.EXTENSION,
            mime=Flac.MIME,
            description=Flac.DESCRIPTION
        )

    @staticmethod
    def check(buf):
        return (len(buf) > 4 and
                buf[0] == 0x66 and
                buf[1] == 0x4C and
                buf[2] == 0x61 and
                buf[3] == 0x43)


class M4a(Extension):
    EXTENSION = 'm4a'
    MIME = 'audio/m4a'
    DESCRIPTION = 'Apple Lossless Audio Codec file'

    def __init__(self):
        super(M4a, self).__init__(
            extension=M4a.EXTENSION,
            mime=M4a.MIME,
            description=M4a.DESCRIPTION
        )

    @staticmethod
    def check(buf):
        return (len(buf) > 4 and
                buf[4] == 0x66 and
                buf[5] == 0x74 and
                buf[6] == 0x79 and
                buf[7] == 0x70 and
                buf[8] == 0x4D and
                buf[9] == 0x34 and
                buf[10] == 0x41 and
                buf[11] == 0x20)

class Ogg(Extension):
    EXTENSION = 'ogg (oga, ogv, ogx, spx, opus)'
    MIME = 'audio/ogg'
    DESCRIPTION = '	Ogg Vorbis Codec compressed Multimedia file'

    def __init__(self):
        super(Ogg, self).__init__(
            extension=Ogg.EXTENSION,
            mime=Ogg.MIME,
            description=Ogg.DESCRIPTION
        )

    @staticmethod
    def check(buf):
        return (len(buf) > 4 and
                buf[0] == 0x4F and
                buf[1] == 0x67 and
                buf[2] == 0x67 and
                buf[3] == 0x53)

class Amr(Extension):
    EXTENSION = 'amr'
    MIME = 'audio/amr'
    DESCRIPTION = 'Adaptive Multi-Rate ACELP (Algebraic Code Excited Linear Prediction) Codec, commonly audio format ' \
                  'with GSM cell phones. '

    def __init__(self):
        super(Amr, self).__init__(
            extension=Amr.EXTENSION,
            mime=Amr.MIME,
            description=Amr.DESCRIPTION
        )

    @staticmethod
    def check(buf):
        return (len(buf) > 5 and
                buf[0] == 0x23 and
                buf[1] == 0x21 and
                buf[2] == 0x41 and
                buf[3] == 0x4D and
                buf[4] == 52)