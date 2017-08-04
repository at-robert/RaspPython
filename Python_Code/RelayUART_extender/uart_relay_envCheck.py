import sys
import time
import serial
import binascii

ser = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

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

# def open_com(b = 9600):
# 	print "Open COM"
# 	ser = serial.Serial(
#     	port='/dev/ttyUSB0',
#     	baudrate=b,
#     	parity=serial.PARITY_NONE,
#     	stopbits=serial.STOPBITS_ONE,
#     	bytesize=serial.EIGHTBITS
# 	)
# 	return;

def close_com():
	ser.close()
	return;


# MAIN

print("VIN and GND should be connected to 12V ........")
# Init
# open_com()

close_relay(1)
close_relay(2)
close_relay(3)
close_relay(4)

# Port 1 On/Off test
print("Port 1 on off test")
open_relay(1)
time.sleep(2)
close_relay(1)
time.sleep(2)

# Port 2 On/Off test
print("Port 2 on off test")
open_relay(2)
time.sleep(2)
close_relay(2)
time.sleep(2)

# Port 3 On/Off test
print("Port 3 on off test")
open_relay(3)
time.sleep(2)
close_relay(3)
time.sleep(2)

# Port 4 On/Off test
print("Port 4 on off test")
open_relay(4)
time.sleep(2)
close_relay(4)
time.sleep(2)

print("If the UART relay hardware is working properly, you should hear a several click sound to indicate relay is switching")

close_com()