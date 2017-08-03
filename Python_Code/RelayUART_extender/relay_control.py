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

# Get status
print "Get Relay status"
command = b"\x55\x56\x00\x00\x00\x00\x00\xAB"
ser.write(command)
result = ser.read(8)
r = binascii.hexlify(result)
print(r.decode('ascii'))

time.sleep(0.1)

# Relay1 Open
print "Relay 1 Open"
command = b"\x55\x56\x00\x00\x00\x01\x02\xAE"
ser.write(command)
result = ser.read(8)
r = binascii.hexlify(result)
print(r.decode('ascii'))

time.sleep(0.1)

# Relay1 Close
print "Relay 1 Close"
command = b"\x55\x56\x00\x00\x00\x01\x01\xAD"
ser.write(command)
result = ser.read(8)
r = binascii.hexlify(result)
print(r.decode('ascii'))

time.sleep(0.1)

ser.close()
