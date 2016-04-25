#Follow steps on http://www.civrays.com/myrobot/news/pythoncgi

#Python script to place in /usr/lib/cgi-bin directory

#! /usr/bin/env python

import cgi
import serial

def arduino(cmd):  
    ser = serial.Serial('/dev/ttyACM0') #USB
    ser.write(cmd + "\n")
    ser.close

data = cgi.FieldStorage()
if "q" in data:
    q = data["q"].value
    arduino(q)
