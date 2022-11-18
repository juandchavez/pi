import time
import serial
from time import sleep

ser = serial.Serial("/dev/ttyS0", 115200)  # Open port with baud rate
serReceive = serial.Serial("/dev/ttyS0", 115200)  # Open port with baud rate
counter = 0
while 1:
    # test = "Test"
    # ser.write(b'khush is gay')
    # time.sleep(.1)
    # print("Test")
    # counter += 1
    print(ser.read(1))
ser.write(b'false')
