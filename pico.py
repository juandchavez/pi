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

def pico_send(txData):
    # Append the CR byte to signal the end of string
    # easier for Pico decode
    txData = txData + '\r'
    # Send to Pico
    ser.write(txData.encode('utf-8'))
    # wait for a bit 
    time.sleep(1)

def pico_recieve():
    # The data buffer
    rxData = bytes()
    # Holds a byte
    rxByte = bytes()
    # The final output of the data recieved
    rxOutput = ''
    # While there is data on the serial ports
    while ser.inWaiting() > 0:
        # Scan the byte
        rxByte = ser.read(1)
        # Add it to the data buffer
        rxData += rxByte
        # Check for the CR byte b'\r'
        if rxByte == b'\r':
            # Decode the buffer
            rxOutput = rxData.decode('utf-8')
            # Get rid of the CR byte
            rxOutput.replace('\r', '')
            print("out: " + rxOutput)
            # Reset the RX values
            rxData = b''
            rxByte = b''
    return rxOutput