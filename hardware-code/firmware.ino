#include <AFMotor.h>

AF_DCMotor backright(4, MOTOR34_64KHZ); // create motor #2, 64KHz pwm
AF_DCMotor backleft(3, MOTOR12_64KHZ);
AF_DCMotor frontleft(2, MOTOR12_64KHZ);
AF_DCMotor frontright(1, MOTOR12_64KHZ);

void go(){
  frontleft.run(FORWARD);
  backleft.run(FORWARD);
  backright.run(FORWARD);
  frontright.run(FORWARD);
}

void reverse(){
  backleft.run(BACKWARD);
  backright.run(BACKWARD);
  frontleft.run(BACKWARD);
  frontright.run(BACKWARD);
}

void left(){
  frontleft.run(FORWARD);
  backleft.run(FORWARD);
  backright.run(RELEASE);
  frontright.run(FORWARD);
}

void right(){
  frontleft.run(FORWARD);
  backleft.run(RELEASE);
  backright.run(FORWARD);
  frontright.run(FORWARD);
}

void bright(){
  backleft.run(BACKWARD);
  backright.run(BACKWARD);
  frontleft.run(RELEASE);
  frontright.run(BACKWARD);
}

void bleft(){
  backleft.run(BACKWARD);
  backright.run(BACKWARD);
  frontleft.run(BACKWARD);
  frontright.run(RELEASE);
}

void chill(){
  backleft.run(RELEASE);
  frontleft.run(RELEASE);
  frontright.run(RELEASE);
  backright.run(RELEASE);
}
void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Motor test!\n");
  
  backright.setSpeed(255);     // set the speed to 200/255
  backleft.setSpeed(255);
  frontleft.setSpeed(255);
  frontright.setSpeed(255);
}

void loop() {
  String command = Serial.readString();
  if (command=="go") {
        go();
        Serial.println(command);
        return;
    }
    else if (command=="reverse") {
        reverse();
        Serial.println(command);
        return;
    }
    else if (command=="chill"){
        chill();
        Serial.println(command);
        return;
    }    
    else if (command=="left"){
        left();
        Serial.println(command);
        return;
    }    
    else if (command=="right") {
        right();
        Serial.println(command);
        return;
    }
        else if (command=="bright") {
        bright();
        Serial.println(command);
        return;
    }
        else if (command=="bleft") {
        bleft();
        Serial.println(command);
        return;
    }
    else{
        Serial.println(command+" IS NOT VALID");
        return;
    }
}
