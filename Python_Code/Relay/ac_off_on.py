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

    while 1:
        #time.sleep(25+random.randint(0,25))
        GPIO.output(37,True)
        print("GPIO37 ON")
	#GPIO.output(38,True)
        time.sleep(3)
        GPIO.output(37,False)
        print("GPIO37 OFF")
        time.sleep(3)
	#GPIO.output(38,False)


#----------------------------------------------------------------------
if __name__ == "__main__":

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT)
    #GPIO.setup(38, GPIO.OUT)
    #GPIO.setup(40, GPIO.OUT)
    
    vizio_SB_Ac_off_on()

