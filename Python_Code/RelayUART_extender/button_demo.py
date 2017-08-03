import sys
import time
import serial
import binascii

def read_return_data(s):
	print "Return data"
	result = ser.read(len)
	r = binascii.hexlify(result)
	print(r.decode('ascii'))
	return;

# Get Relay status function
def get_relay_status(parameter = 0):
	print "Get Relay status"
	command = b"\x55\x56\x00\x00\x00\x00\x00\xAB"			
	ser.write(command)
	return;

# Open Relay function
def open_relay(relay_num):
	print("Open Relay %d\r\n", relay_num)
	if(relay_num == 1):
		command = b"\x55\x56\x00\x00\x00\x01\x01\xAD"
	elif(relay_num == 2):
		command = b"\x55\x56\x00\x00\x00\x02\x01\xAE"
	elif(relay_num == 3):
		command = b"\x55\x56\x00\x00\x00\x03\x01\xAF"
	elif(relay_num == 4):
		command = b"\x55\x56\x00\x00\x00\x04\x01\xB0"
	
	ser.write(command)
	return;


# Close Relay function
def close_relay(relay_num):
	print("Close Relay %d\r\n", relay_num)
	if(relay_num == 1):
		command = b"\x55\x56\x00\x00\x00\x01\x02\xAE"
	elif(relay_num == 2):
		command = b"\x55\x56\x00\x00\x00\x02\x02\xAF"
	elif(relay_num == 3):
		command = b"\x55\x56\x00\x00\x00\x03\x02\xB0"
	elif(relay_num == 4):
		command = b"\x55\x56\x00\x00\x00\x04\x02\xB1"
	
	ser.write(command)
	return;

def open_com(b = 9600):
	print "Open COM"
	ser = serial.Serial(
    	port='/dev/ttyUSB0',
    	baudrate=b,
    	parity=serial.PARITY_NONE,
    	stopbits=serial.STOPBITS_ONE,
    	bytesize=serial.EIGHTBITS
	)

	return;

def close_com():
	ser.close()
	return;


# MAIN

# Init
open_com()

close_relay(1)
close_relay(2)
close_relay(3)
close_relay(4)

open_relay(1)
time.sleep(0.5)
close_relay(1)

open_relay(1)
time.sleep(0.5)
close_relay(1)

close_com()