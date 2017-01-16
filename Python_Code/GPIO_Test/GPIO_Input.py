import re
import os
import sys
import shutil
import chardet
import time
import RPi.GPIO as GPIO

#----------------------------------------------------------------------
def GPIO_IntDet(int_num):

    GPIO.setmode(GPIO.BOARD)
    print "GPIO input pin = %d" %(int(int_num))
    GPIO.setup(int(int_num), GPIO.IN)

    while 1:
        time.sleep(1)
        input_val = GPIO.input(int(int_num))
        print " GPIO PIN = %d" %(input_val)

#----------------------------------------------------------------------
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print 'no argument; Usage: GPIO_Input.py PIN_NUM'
        sys.exit()

    GPIO_IntDet(sys.argv[1])
    

