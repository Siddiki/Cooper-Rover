#include "application.h"                                            //libraries
#include "Adafruit-MotorShield-V2/Adafruit-MotorShield-V2.h"
#include "Adafruit-MotorShield-V2/Adafruit_PWMServoDriver.h"

#define SPEED 255
#define TIME 2500



Adafruit_MotorShield AFMS = Adafruit_MotorShield();             //Initialize Motors
Adafruit_DCMotor *Motor1 = AFMS.getMotor(1);
Adafruit_DCMotor *Motor2 = AFMS.getMotor(2);
Adafruit_DCMotor *Motor3 = AFMS.getMotor(3);
Adafruit_DCMotor *Motor4 = AFMS.getMotor(4);
    
void forward(){                                                 //Defining functions
    Motor1->run(FORWARD);
    Motor2->run(FORWARD);
    Motor3->run(FORWARD);
    Motor4->run(FORWARD);
    
    return;
}

void reverse(){
    Motor1->run(BACKWARD);
    Motor2->run(BACKWARD);
    Motor3->run(BACKWARD);
    Motor4->run(BACKWARD);
    
    return;
}

void stop(){
    Motor1->run(RELEASE);
    Motor2->run(RELEASE);
    Motor3->run(RELEASE);
    Motor4->run(RELEASE);
    
    return;
}

void left() {
    
    Motor3->run(FORWARD);
    Motor4->run(FORWARD);

    return;
}

void right(){
    
    Motor1->run(FORWARD);
    Motor2->run(FORWARD);
    
    return;
    
}


void setup() {

    AFMS.begin();
    Motor1->setSpeed(SPEED);                                        //Initialize motor speeds
    Motor2->setSpeed(SPEED);
    Motor3->setSpeed(SPEED);
    Motor4->setSpeed(SPEED);
    Spark.function("direction",direction);                          //Spark function to use internet data


}



void loop() {
    
   
}

int direction(String command){                                      //Spark function 
    
    if (command=="forward") {
        forward();
        return 4;
    }
    else if (command=="reverse") {
        reverse();
        return 3;
    }
    else if (command=="stop"){
        stop();
        return 2;
    }    
    else if (command=="left"){
        left();
        return 1;
    }    
    else if (command=="right") {
        right();
        return 0;
    }
    else{
        return -1;
    }

}


