import numpy
import pyaudio
import analyse

# Initialize PyAudio
pyaud = pyaudio.PyAudio()

# Open input stream, 16-bit mono at 44100 Hz
# On my system, device 4 is a USB microphone
stream = pyaud.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 44100,
    input_device_index = 2,
    input = True)

while True:
    # Read raw microphone data
    try:
    	rawsamps = stream.read(1024)
    except IOError:
        pass
    # Convert raw data to NumPy array
    samps = numpy.fromstring(rawsamps, dtype=numpy.int16)
    # Show the volume and pitch
    print analyse.loudness(samps), analyse.musical_detect_pitch(samps)