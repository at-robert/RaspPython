import re
import os
import sys
import shutil
import chardet
import time
import RPi.GPIO as GPIO
import random

#----------------------------------------------------------------------
def vizio_SB_Ac_off_on():
    loop_count = 0
    while 1:
        print("Loop count = %s"%(loop_count))
	os.system('irsend SEND_ONCE VIZIO_TV KEY_POWER')
        print("Turn VIZIO TV off and wait for 30 seconds")
        time.sleep(30)
        #time.sleep(25+random.randint(0,25))
        GPIO.output(37,False)
        print("Wifi Off wait for 30 seconds")
        time.sleep(30)
        GPIO.output(37,True)
        print("Wifi On wait for 60 seconds")
        time.sleep(60)
        GPIO.output(37,False)
        print("Wifi Off wait for 30 seconds")
        time.sleep(30)
        GPIO.output(37,True)
        print("Wifi On wait for 60 seconds")
        time.sleep(60)
        GPIO.output(37,False)
        print("Wifi Off wait for 30 seconds")
        time.sleep(30)
        GPIO.output(37,True)
        print("Wifi On wait for 60 seconds")
        time.sleep(60)
        GPIO.output(37,False)
        print("Wifi Off wait for 30 seconds")
        time.sleep(30)
        GPIO.output(37,True)
        print("Wifi On wait for 60 seconds")
        time.sleep(60)
        
	#GPIO.output(38,False)
        os.system('irsend SEND_ONCE VIZIO_TV KEY_POWER')
        time.sleep(5)
        os.system('irsend SEND_ONCE VIZIO_TV KEY_POWER')
        print("Turn VIZIO TV on and wait for 60 seconds")
        time.sleep(60)
        loop_count = loop_count + 1


#----------------------------------------------------------------------
if __name__ == "__main__":

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT)
    #GPIO.setup(38, GPIO.OUT)
    #GPIO.setup(40, GPIO.OUT)
    
    vizio_SB_Ac_off_on()

