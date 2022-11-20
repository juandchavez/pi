import io
import time
import serial
from time import sleep
from locker import locker_system

ser = serial.Serial(port ='/dev/ttyS0',  # type: ignore
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


# Init Locker Network
locker_network = locker_system()
locker = "qkMOyDPLnlNYSihFOVDT"

# while 1:
#     print(counter == 1)
#     if counter == 1:
#         txData = 'true\r'
#         print("---- PICO Write  ----\n")
#         ser.write(txData.encode('utf-8'))
#         # counter += 1
#         time.sleep(1)
    
#     if ser.inWaiting() > 0:
#         print("---- PICO Read ----\n")
#         # Scan the byte
#         rxScan = ser.read(1)
#         # Add it to the data buffer
#         rxData += rxScan
#         # Check for the CR byte b'\r'
#         print(rxScan)
#         if rxScan == b'\r':
#             # Decode the buffer
#             rxOutput = rxData.decode('utf-8')
#             # Print the PICO data
#             print("out: " + rxOutput)
#             # TODO: Email validation
#             response = locker_network.useLocker(locker, rxOutput)
#             print(response)
#             # Reset the RX values
#             rxData = b''
#             rxScan = b''
#             rxOutput = ''
#             # TODO: Conditional on locker response
            

print(counter == 1)
if counter == 1:
    txData = 'true\r'
    print("---- PICO Write  ----\n")
    ser.write(txData.encode('utf-8'))
    # time.sleep(5)
    # txData = 'false\r'
    # print("---- PICO Write  ----\n")
    # ser.write(txData.encode('utf-8')) 

    
    
    
