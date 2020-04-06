import wave
import pyaudio
import numpy as np
import pylab
import time

RATE = 44100
CHUNK = int(RATE / 20)
FILENAME = 'audio.wav'


def soundplot(stream):
    t1 = time.time()
    data = np.fromstring(stream.readframes(CHUNK), dtype=np.int16)
    pylab.plot(data)
    pylab.title(i)
    pylab.grid()
    pylab.axis([0, len(data), -2 ** 16 / 2, 2 ** 16 / 2])
    pylab.savefig("03.png", dpi=50)
    pylab.close('all')
    print("took %.02f ms" % ((time.time() - t1) * 1000))


audioFile = wave.open(FILENAME, 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(audioFile.getsampwidth()),
                channels=audioFile.getnchannels(),
                rate=audioFile.getframerate(),
                output=True)

data = audioFile.readframes(CHUNK)

for i in range(int(20 * RATE / CHUNK)):  # do this for 10 seconds
    soundplot(stream)

'''
    
while data != '':
    #stream.write(data)
    #data = audioFile.readframes(CHUNK)
    data = np.fromstring(audioFile.readframes(CHUNK), dtype=np.int16)
    peak = np.average(np.abs(data)) * 2
    bars = "#" * int(50 * peak / 2 ** 16)
    print("%05d %s" % (peak, bars))

'''
########################
stream.stop_stream()
stream.close()

p.terminate()
