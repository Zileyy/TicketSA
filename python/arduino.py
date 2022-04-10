# Ajnur Bogucanin | Graficari | for HackAtHome2022

# Arduino.py is going to get information form Arudino that we need.
# That information is NFC card ID. With what we can confirm if user
# has a valid ticket on account.

#

#IMPORTS
import serial       #Serial is used for reading serial ports
import os

#VARS
removes = ['\'','b',' ','\r','\n']

#MAIN

#Function that read and cleans data from serial port to obtain valid card ID
def readCard(port):
    #read serial port
    ser = serial.Serial(str(port), 9800, timeout=1)
    ser.flushInput()
    while True:  
        ser_bytes = ser.readline()
        if len(ser_bytes) >= 5:
            break
    
    #decode from bytes to str
    ser_bytes = ser_bytes.decode()                  

    #remove all elements from list 'removes' so we get cleaner ID
    for x in removes:
        ser_bytes.replace('b'+x,'')

    #removes spaces
    ser_bytes = ser_bytes.replace(' ','')
    ser_bytes = ser_bytes.replace('%','')

    ser_bytes = os.linesep.join([s for s in ser_bytes.splitlines() if s])
    return ser_bytes
