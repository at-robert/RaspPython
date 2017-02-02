import re
import os
import sys
import shutil
import chardet
import time
import RPi.GPIO as GPIO
import numpy
import pyaudio
import analyse

# Initialize PyAudio
pyaud = pyaudio.PyAudio()
CHUNK = 4096

# Open input stream, 16-bit mono at 44100 Hz
# On my system, device 4 is a USB microphone
stream = pyaud.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 44100,
    input_device_index = 2,
    input = True,
    frames_per_buffer=CHUNK)

#----------------------------------------------------------------------
def sound_det():
    count = 0
    print "Sound Check!!"

    while True:
        # Read raw microphone data
        try:
           rawsamps = stream.read(CHUNK)
    	except IOError:
           pass
        # Convert raw data to NumPy array
        samps = numpy.fromstring(rawsamps, dtype=numpy.int16)
        # Show the volume and pitch
        if(analyse.loudness(samps) > -10) & (count > 10):
            print "Sound Detected"
            break
        else:
            if(count > 10):
                print "No Sound Detected"
        count =  count + 1

#----------------------------------------------------------------------
def vizio_SB_2820_Loop():
    count = 0
    print "Start vizio sound bar 2820 Power On/Off loop test"

    while 1:
        time.sleep(3)
        os.system('irsend SEND_ONCE VIZIO_SB KEY_POWER')
        count = count + 1
        print "LOOP COUNT = %d" %(count)

#----------------------------------------------------------------------
def vizio_SB_3251_Loop():
    count = 0
    print "Start vizio sound bar 3251 Power On/Off loop test"

    while 1:
        time.sleep(4)
        os.system('irsend SEND_ONCE VIZIO_SB KEY_POWER')
        count = count + 1
        print "LOOP COUNT = %d" %(count)
        sound_det()


#----------------------------------------------------------------------
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print 'no argument; Usage: vizio_sb_loop.py 3251'
        sys.exit()

    if(sys.argv[1] == '3251'):
        vizio_SB_3251_Loop()
    else:
        vizio_SB_2820_Loop()
    

