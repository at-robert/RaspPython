import re
import os
import sys
import shutil
import chardet
import time
import RPi.GPIO as GPIO
import random

# To setup basic delay time offset
delay_offset = 0

#----------------------------------------------------------------------
def _dc_power_cycling(count):
    for i in range(0,count):
        source_switch_time(2)
        os.system('irsend SEND_ONCE TWN_TV KEY_POWER')
        print ("DC off")
        source_switch_time(5)
        os.system('irsend SEND_ONCE TWN_TV KEY_POWER')
        print ("DC on")
        print(" DC loop in {}".format(i))    

#----------------------------------------------------------------------
def source_switch_time(t):
    random_t = delay_offset+random.randint(0,3)+t
    print ("Random Time = %d"%(random_t))
    time.sleep(random_t)

#----------------------------------------------------------------------
def _ac_power_cycling():
    GPIO.output(37,True)
    print ("AC OFF!!")
    source_switch_time(2)
    GPIO.output(37,False)
    print ("AC ON!!")
    source_switch_time(8)
    os.system('irsend SEND_ONCE TWN_TV KEY_POWER')
    print ("Send IR Power Key!!")
    source_switch_time(10)

#----------------------------------------------------------------------
def msd92q_Loop(_pwr_test):
    count = 0
    print ("Start TWN TV MSD92Q loop test for input menu")

    while 1:
        # if(_pwr_test == 1):
        #     print ("AC Test")
        #     _ac_power_cycling()

        source_switch_time(5)
        os.system('irsend SEND_ONCE TWN_TV KEY_INPUT')
        print ("Open input menu")
        source_switch_time(0.5)
        os.system('irsend SEND_ONCE TWN_TV KEY_INPUT')
        print ("Open input menu")
        source_switch_time(1)
        os.system('irsend SEND_ONCE TWN_TV KEY_DOWN')
        print ("DOWN")
        source_switch_time(1)
        os.system('irsend SEND_ONCE TWN_TV KEY_ENTER')
        print ("Switch to other source")

        source_switch_time(5)
        os.system('irsend SEND_ONCE TWN_TV KEY_INPUT')
        print ("Open input menu")
        source_switch_time(0.5)
        os.system('irsend SEND_ONCE TWN_TV KEY_INPUT')
        print ("Open input menu")
        source_switch_time(1)
        os.system('irsend SEND_ONCE TWN_TV KEY_UP')
        print ("DOWN")
        source_switch_time(1)
        os.system('irsend SEND_ONCE TWN_TV KEY_ENTER')
        print ("Switch to other source")


        count = count + 1
        print ("LOOP COUNT = %d" %(count))

        # _dc_power_cycling(5)

#----------------------------------------------------------------------
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print ('no argument; Usage: TWN_TV_loop.py x')
        sys.exit()

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT)


    msd92q_Loop(0)
    print(" AC Off/On test is off, input test")

