#include "application.h"
#include "Adafruit-MotorShield-V2/Adafruit-MotorShield-V2.h"
#include "Adafruit-MotorShield-V2/Adafruit_PWMServoDriver.h"

#DEFINE SPEED 255
#DEFINE TIME 2500


    Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
    Adafruit_DCMotor *Motor1 = AFMS.getMotor(1);
    Adafruit_DCMotor *Motor2 = AFMS.getMotor(2);
    Adafruit_DCMotor *Motor3 = AFMS.getMotor(3);
    Adafruit_DCMotor *Motor4 = AFMS.getMotor(4);


void setup() {

    AFMS.begin();
    Motor1->setSpeed(SPEED);
    Motor2->setSpeed(SPEED);
    Motor3->setSpeed(SPEED);
    Motor4->setSpeed(SPEED);

}

void loop() {
    
    Motor1->run(FORWARD);
    Motor2->run(FORWARD);
    Motor3->run(FORWARD);
    Motor4->run(FORWARD);
    
    delay(TIME);
    
    Motor1->run(BACKWARD);
    Motor2->run(BACKWARD);
    Motor3->run(BACKWARD);
    Motor4->run(BACKWARD);
    
    delay(TIME);
    
    Motor1->run(RELEASE);
    Motor2->run(RELEASE);
    Motor3->run(RELEASE);
    Motor4->run(RELEASE);
    
    delay(TIME);

}
