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
    print "Start vizio sound bar 2820 Demo 2 loop test"

    while 1:
        time.sleep(3)
        os.system('irsend SEND_ONCE VIZIO_SB KEY_POWER')
        time.sleep(5)
        os.system('irsend SEND_ONCE VIZIO_SB KEY_INPUT_AUX_1')
        count = count + 1
        print "LOOP COUNT = %d" %(count)

#----------------------------------------------------------------------
def vizio_SB_3251_Loop():
    count = 0
    print "Start vizio sound bar 3251 Demo 2 loop test"

    while 1:
        time.sleep(4)
        os.system('irsend SEND_ONCE VIZIO_SB KEY_POWER')
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
    

