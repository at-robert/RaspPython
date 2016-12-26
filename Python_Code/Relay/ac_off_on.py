import re
import os
import sys
import shutil
import chardet
import time
import RPi.GPIO as GPIO

#----------------------------------------------------------------------
def vizio_SB_Ac_off_on():

    while 1:
        time.sleep(10)
        GPIO.output(37,True)
        time.sleep(5)
        GPIO.output(37,False)



#----------------------------------------------------------------------
if __name__ == "__main__":

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT)
    GPIO.setup(38, GPIO.OUT)
    GPIO.setup(40, GPIO.OUT)
    
    vizio_SB_Ac_off_on()

