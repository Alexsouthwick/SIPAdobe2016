#include <Servo.h>

Servo servoRight;
Servo servoLeft;

void setup() {
  // put your setup code here, to run once:
  servoLeft.attach(12);
  servoRight.attach(11);
  //clockwise: 1300
  //counterclockwise: 1700 
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
}

void loop() {
  sway();
  left();
  delay(2000);
  for(int i = 0; i < 4; i++){
    runningMan();
    left();
    delay(2200);
  }
}
void forward() {
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
}
void backward() {
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1700);
}
void left() {
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1300);
}
void right() {
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1700);
}
void runningMan(){
  for(int i = 0; i < 13; i++){
    forward();
    delay(100);
    backward();
    delay(100); 
  }
}
void sway(){
  for(int i = 0; i < 2; i++){
     forward();
     delay(2000);
     backward();
     delay(2000);
     left();
     delay(800);
     forward();
     delay(2000);
     backward();
     delay(2000);
     right();
     delay(2000);
     forward();
     delay(2000);
     backward();
     delay(2000);
  }  
}




