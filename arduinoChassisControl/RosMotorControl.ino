/*
 * rosserial Servo Control Example
 *
 * This sketch demonstrates the control of hobby R/C servos
 * using ROS and the arduiono
 * 
 * For the full tutorial write up, visit
 * www.ros.org/wiki/rosserial_arduino_demos
 *
 * For more information on the Arduino Servo Library
 * Checkout :
 * http://www.arduino.cc/en/Reference/Servo
 */

#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif

#include <ros.h>
#include <std_msgs/Int16.h>

ros::NodeHandle  nh;

int fleft = 7;
int rleft = 6;
int sleft = 11;
int fright = 12;
int rright = 13;
int sright = 5;

void leftCallBack( const std_msgs::Int16& cmd_msg){
  
  if(cmd_msg.data > 0 && cmd_msg.data < 255){
     digitalWrite(fleft, HIGH);
     digitalWrite(rleft, LOW);
     analogWrite(sleft, cmd_msg.data);
     
  }else if(cmd_msg.data < 0 && cmd_msg.data > -255){
     digitalWrite(fleft, LOW);
     digitalWrite(rleft, HIGH);
     analogWrite(sleft, -cmd_msg.data);
  }else{
    digitalWrite(fleft, LOW);
     digitalWrite(rleft, LOW);
     analogWrite(sleft, 0);
  }
}

void rightCallBack( const std_msgs::Int16& cmd_msg){
  
  if(cmd_msg.data > 0 && cmd_msg.data < 255){
     digitalWrite(fright, HIGH);
     digitalWrite(rright, LOW);
     analogWrite(sright, cmd_msg.data);
     
  }else if(cmd_msg.data < 0 && cmd_msg.data > -255){
     digitalWrite(fright, LOW);
     digitalWrite(rright, HIGH);
     analogWrite(sright, -cmd_msg.data);
  }else{
    digitalWrite(fright, LOW);
     digitalWrite(rright, LOW);
     analogWrite(sright, 0);
  }
}


ros::Subscriber<std_msgs::Int16> subl("left", leftCallBack);
ros::Subscriber<std_msgs::Int16> subr("right", rightCallBack);

void setup(){
  pinMode(fleft, OUTPUT);
  pinMode(rleft, OUTPUT);
  pinMode(sleft, OUTPUT);
  pinMode(fright, OUTPUT);
  pinMode(rright, OUTPUT);
  pinMode(sright, OUTPUT);

  nh.initNode();
  nh.getHardware()->setBaud(9600);
  nh.subscribe(subl);
  nh.subscribe(subr);
  
}

void loop(){
  nh.spinOnce();
  delay(1);
}
