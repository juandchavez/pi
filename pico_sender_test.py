import io
import time
import serial
from time import sleep
import pyrebase

ser = serial.Serial(port ='/dev/ttyS0',
                    baudrate = 115200,
                    parity = serial.PARITY_NONE,
                    stopbits = serial.STOPBITS_ONE,
                    bytesize = serial.EIGHTBITS,
                    timeout = 1)  # Open port with baud rate
counter = 1
# To sent to PICO
# Keep as CHAR for encode
txData = ''

# To recieve from PICO
rxData = bytes()
rxScan = bytes()
rxOutput = ''

while 1:
    
    if counter == 1:
        txData = 'true\r'
        print("---- PICO Write  ----\n")
        ser.write(txData.encode('utf-8'))
        counter += 1
        time.sleep(1)
    
    if ser.inWaiting() > 0:
        print("---- PICO Read ----\n")
        # Scan the byte
        rxScan = ser.read(1)
        # Add it to the data buffer
        rxData += rxScan
        # Check for the CR byte b'\r'
        print(rxScan)
        if rxScan == b'\r':
            # Decode the buffer
            rxOutput = rxData.decode('utf-8')
            # Print the PICO data
            print("out: " + rxOutput)
            # Reset the RX values
            rxData = b''
            rxScan = b''
            rxOutput = ''
            
    
    
    
    
