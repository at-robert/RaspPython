import re
import os
import sys
import shutil
import chardet
import time
import RPi.GPIO as GPIO

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
	GPIO.output(37,False)
	print ("AC ON!!")
        time.sleep(15)
        os.system('irsend SEND_ONCE VIZIO_SB KEY_POWER')
	print ("Send IR Power Key!!")
        count = count + 1
        print "LOOP COUNT = %d" %(count)
	time.sleep(15)
	GPIO.output(37,True)
	print ("AC OFF!!")
	time.sleep(10)

#----------------------------------------------------------------------
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print 'no argument; Usage: vizio_sb_loop.py 3251'
        sys.exit()

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT)

    if(sys.argv[1] == '3251'):
        vizio_SB_3251_Loop()
    else:
        vizio_SB_2820_Loop()
