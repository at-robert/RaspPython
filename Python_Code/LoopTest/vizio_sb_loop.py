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
	print ("Switch to AUX")
        time.sleep(7)
        os.system('irsend SEND_ONCE VIZIO_SB KEY_INPUT_OPTICAL_4')
	print ("Switch to OPT")
        time.sleep(7)
        os.system('irsend SEND_ONCE VIZIO_SB KEY_INPUT_HDMI_ARC_6')
	print ("Switch to ARC")
        if(count == 0):
            print "Wait for HDMI-ARC communication"
            time.sleep(7)
        time.sleep(7)
        os.system('irsend SEND_ONCE VIZIO_SB KEY_INPUT_USB_7')
	print ("Switch to USB")	
        time.sleep(15)
        os.system('irsend SEND_ONCE VIZIO_SB KEY_INPUT_BLUETOOTH')
	print ("Switch to BT")
        time.sleep(7)
        os.system('irsend SEND_ONCE VIZIO_SB KEY_PLAYPAUSE')
	print ("Press Play_Pause")
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
    

