#Follow steps on http://www.civrays.com/myrobot/news/pythoncgi

#Python script to place in cgi-bin directory

#! /usr/bin/env python

import cgi
import serial

def arduino(cmd):  
    ser = serial.Serial('/dev/ttyAMA0', 9600) #RPI UART
    ser.write(cmd + "\n")
    ser.close

data = cgi.FieldStorage()
if "q" in data:
  q = data["q"].value
	arduino(q)
	
