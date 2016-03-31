
//note: run $ python3 /usr/share/doc/python3-pifacedigitalio/examples/simplewebcontrol.py in pi CLI first

import pifacedigitalio as p
import urllib2
import time

while(1):
	input = urllib2.urlopen("http://cooper-rover.appspot.com/direction?Brake").read()
	if not direction:
		print 'nothing found'
	else:
		print direction

p.init()

switch

case input == go
	p.digital_write(0, 1)
	p.digital_write(1, 1)
	p.digital_write(2, 0)
	p.digital_write(3, 0)
case input == back
	p.digital_write(0, 0)
	p.digital_write(1, 0)
	p.digital_write(2, 1)
	p.digital_write(3, 1)
case input == left
	p.digital_write(0, 1)
	p.digital_write(1, 1)
	p.digital_write(2, 0)
	p.digital_write(3, 1)
case input == right
	p.digital_write(0, 1)
	p.digital_write(1, 1)
	p.digital_write(2, 1)
	p.digital_write(3, 0)
case input == break
	p.digital_write(0, 0)
	p.digital_write(1, 0)
	p.digital_write(2, 0)
	p.digital_write(3, 0)
	
p.deinit()
