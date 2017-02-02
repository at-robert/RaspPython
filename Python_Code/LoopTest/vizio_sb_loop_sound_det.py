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
CHUNK = 1024

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

    while True:
        # Read raw microphone data
        try:
            rawsamps = stream.read(CHUNK)
            # Convert raw data to NumPy array
            samps = numpy.fromstring(rawsamps, dtype=numpy.int16)
            # Show the volume and pitch
            vol = analyse.loudness(samps)

            if(vol > -10) & (count > 10):
                print "Sound Detected"
                break
            else:
                if(count > 100):
                    print "No Sound Detected"
                    time.sleep(4)
                    # os.system('irsend SEND_ONCE VIZIO_SB KEY_POWER')
                    count = 0
            count = count + 1
        except IOError:
           pass

#----------------------------------------------------------------------
def vizio_SB_2820_Loop():
    count = 0
    print "Start vizio sound bar 2820 loop test"

    while 1:
        time.sleep(7)
        os.system('irsend SEND_ONCE VIZIO_SB KEY_INPUT_AUX_1')
        time.sleep(7)
        os.system('irsend SEND_ONCE VIZIO_SB KEY_INPUT_OPTICAL_4')
        time.sleep(7)
        os.system('irsend SEND_ONCE VIZIO_SB KEY_INPUT_USB_7')
        time.sleep(15)
        os.system('irsend SEND_ONCE VIZIO_SB KEY_INPUT_BLUETOOTH')
        time.sleep(7)
        os.system('irsend SEND_ONCE VIZIO_SB KEY_PLAYPAUSE')
        count = count + 1
        print "LOOP COUNT = %d" %(count)

#----------------------------------------------------------------------
def vizio_SB_3251_Loop():
    count = 0
    print "Start vizio sound bar 3251 loop test"

    while 1:
        time.sleep(7)
        os.system('irsend SEND_ONCE VIZIO_SB KEY_INPUT_AUX_1')
        time.sleep(7)
        sound_det()
        os.system('irsend SEND_ONCE VIZIO_SB KEY_INPUT_OPTICAL_4')
        time.sleep(7)
        sound_det()
        os.system('irsend SEND_ONCE VIZIO_SB KEY_INPUT_HDMI_ARC_6')
        if(count == 0):
            print "Wait for HDMI-ARC communication"
            time.sleep(7)
        time.sleep(7)
        sound_det()
        os.system('irsend SEND_ONCE VIZIO_SB KEY_INPUT_USB_7')
        time.sleep(15)
        sound_det()
        os.system('irsend SEND_ONCE VIZIO_SB KEY_INPUT_BLUETOOTH')
        time.sleep(7)
        sound_det()
        os.system('irsend SEND_ONCE VIZIO_SB KEY_PLAYPAUSE')
        count = count + 1
        print "LOOP COUNT = %d" %(count)


#----------------------------------------------------------------------
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print 'no argument; Usage: vizio_sb_loop.py 3251'
        sys.exit()

    if(sys.argv[1] == '3251'):
        vizio_SB_3251_Loop()
    else:
        vizio_SB_2820_Loop()
    

