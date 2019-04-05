import re
import os
import sys
import shutil
import chardet
import time
import RPi.GPIO as GPIO
import random

# To setup basic delay time offset
delay_offset = 3


#----------------------------------------------------------------------
def source_switch_time(t):
    random_t = delay_offset+random.randint(0,3)+t
    print ("Random Time = %d"%(random_t))
    time.sleep(random_t)

#----------------------------------------------------------------------
def _ac_power_cycling():
    GPIO.output(37,True)
    print ("AC OFF!!")
    source_switch_time(5)
    GPIO.output(37,False)
    print ("AC ON!!")
    source_switch_time(15)
    os.system('irsend SEND_ONCE TWN_TV KEY_POWER')
    print ("Send IR Power Key!!")
    source_switch_time(10)

#----------------------------------------------------------------------
def msd92q_Loop(_pwr_test):
    count = 0
    print ("Start TWN TV MSD92Q loop test with AC power cycling")

    while 1:
        if(_pwr_test == 1):
            print ("AC Test")
            _ac_power_cycling()

        source_switch_time(5)
        os.system('irsend SEND_ONCE TWN_TV KEY_HDMI')
        print ("Switch to HDMI")
        source_switch_time(5)
        os.system('irsend SEND_ONCE TWN_TV KEY_HDMI')
        print ("Switch to HDMI2")
        source_switch_time(5)
        os.system('irsend SEND_ONCE TWN_TV KEY_HDMI')
        print ("Switch to HDMI3")
        source_switch_time(5)
        os.system('irsend SEND_ONCE TWN_TV KEY_AV')
        print ("Switch to AV")
        source_switch_time(5)
        os.system('irsend SEND_ONCE TWN_TV KEY_COMP')
        print ("Switch to COMP")
        source_switch_time(5)
        os.system('irsend SEND_ONCE TWN_TV KEY_TV')
        print ("Switch to TV")
        source_switch_time(5)
        os.system('irsend SEND_ONCE TWN_TV KEY_POWER')
        print ("DC off")
        source_switch_time(10)
        os.system('irsend SEND_ONCE TWN_TV KEY_POWER')
        print ("DC on")
        source_switch_time(6)
        count = count + 1
        print ("LOOP COUNT = %d" %(count))

#----------------------------------------------------------------------
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print ('no argument; Usage: TWN_TV_loop.py msd92q')
        sys.exit()

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT)

    if(sys.argv[1] == 'msd92q'):
        msd92q_Loop(1)
        print(" AC Off/On test is on")
    else:
        msd92q_Loop(0)
        print(" AC Off/On test is off")

