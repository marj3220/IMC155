#include <Servo.h>
#include <HCSR04.h>

byte triggerPin = 5;
byte echoPin = 4;
double average_depth = 0;
double depth_storage[10];

Servo myservo;
int val;    // variable to read the value from the analog pin

void setup() {
  // put your setup code here, to run once:
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  Serial.begin(9600);
  HCSR04.begin(triggerPin, echoPin);
  byte i = 0;
  while(i<11){
    double* temp_distances = HCSR04.measureDistanceCm();
    i = i + 1;
    average_depth = temp_distances[0];
    delay(20);
    }
  average_depth = average_depth/10;
}

void loop() {
  // put your main code here, to run repeatedly:
  double* distances = HCSR04.measureDistanceCm();
  Serial.print("1: ");
  Serial.print(distances[0]);
  Serial.println(" cm");
  update_storage(distances[0]);
  average_depth = calculate_average();
  Serial.println("---");
  Serial.println(average_depth);
  val = map(distances[0], average_depth+1.0, 50, 0, 180);     // scale it for use with the servo (value between 0 and 180)
  myservo.write(val);                  // sets the servo position according to the scaled value
  delay(125);         
}

void update_storage(double recent_val) {
  double temp_storage[10];
  for(byte i = 9; i>0; i--){
    depth_storage[i] = depth_storage[i-1];
   }
   depth_storage[0] = recent_val;
  }

double calculate_average() {
  double temp_value = 0;
  for(int i = 0; i<9; i++){
    temp_value = temp_value + depth_storage[i];
    }
  return temp_value/10;
  
  }
