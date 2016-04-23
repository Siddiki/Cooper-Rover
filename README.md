# Cooper-Rover

Built a rover which can be controlled through a web app. http://www.cooper-rover.appspot.com

Webapp-code:

-Contains our sites HTML/CSS/Javascript

-Appended vlc player stream from the Raspberry Pi 2

-Depending upon the keycodes selected (up, down, right, left), sent appropriate data to the Raspberry Pi 2. 

Hardware code: 

-Recieved data, controlled by user keyboard input, through a Python CGI script, written on the Raspberry Pi 2, which is running a Apache 2 Webserver. The script reads in the data and sends the data to the Arduino using the Serial Port. 

-Depending upon the serial input, the Arduino motorscript controls the motors appropriately

-The Bash script, when configured appropriately, automatically streams to a VLC player accessible on the network. 

Main Difficulties:

The main difficulty was dealing with the fact that the streaming and the command processing must be as realtime as possible for proper control of the car. This caused for optimizations to have to be made, including purchasing the Raspberry Pi Camera Module for the sole reason that it is capable of streaming H.264 video. 

Further Work: 

We would like our project to serve as a Blackbox application. If the Rover-Arduino-Raspberry Pi-Camera setup, with all appropriate code programmed, were purchased, if one were to go to our site, they would be able to register themselves and utilize our stream-control services. 

Our website, which is hosted on Google App Engine, has google login functionality already implemented, which enables database registration. Furthermore, an LCD screen would be placed upon the car, which would detail the registration code needed to register the setup. Lastly, the code would need to be fine-tuned such that there is little effort required by the user to configure his/her hardware setup. 

