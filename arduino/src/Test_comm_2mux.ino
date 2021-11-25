#include <Wire.h>
#include "Adafruit_HTU31D.h"
#include "Adafruit_SGP30.h"
#include "SparkFun_I2C_Mux_Arduino_Library.h"

#define SLAVE_ADDRESS 0x08

Adafruit_HTU31D **temperature_sensors;
QWIICMUX mux70;
//QWIICMUX mux71;

const int nb_sensors = 6;
const int nb_sensors_mux = 3;
float float_matrix[nb_sensors] = {0};
char data[7];
int j = 99;

byte zero = 0;
byte sept = 7;

void setup() 
{
  Serial.begin(115200);
  //Wire.begin();
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  while (!Serial) {
    delay(100); // wait till serial port opens
  }
  
  if (mux70.begin(0x70,Wire) == false){
    Serial.println("Mux not detected. Freezing...");
    while (1)
      ;
  }
  Serial.println("Both mux detected");

  temperature_sensors = new Adafruit_HTU31D *[nb_sensors];
  for (int x=0 ; x<nb_sensors ; x++){
    temperature_sensors[x] = new Adafruit_HTU31D();
  }

  mux70.setPort(0);
  Serial.println("verify mux70 port 0");
  if (!temperature_sensors[0]->begin(0x41)){
    Serial.println("Couldn't find sensor!");
    while (1);
  }
  mux70.setPort(7);
  Serial.println("verify mux70 port 7");
  if (!temperature_sensors[1]->begin(0x40) || !temperature_sensors[2]->begin(0x41)){
    Serial.println("Couldn't find sensor!");
    while (1);
  }
  delay(500);
  mux70.setPort(3);
  Serial.println("verify mux70 port 3");
  if (!temperature_sensors[3]->begin(0x40)){
    Serial.println("Couldn't find sensor!");
    while (1);
  }
  mux70.setPort(4);
  Serial.println("verify mux70 port 6");
  if (!temperature_sensors[4]->begin(0x40) || !temperature_sensors[5]->begin(0x41)){
    Serial.println("Couldn't find sensor!");
    while (1);
  }
}

void loop(){
  Serial.println("capteur 0");
  mux70.setPort(0);
  sensors_event_t humidity,temp;
  temperature_sensors[0]->getEvent(&humidity, &temp);
  float_matrix[0] = temp.temperature;
  Serial.println(float_matrix[0]);

  Serial.println("capteur 1");
  mux70.setPort(7);
  sensors_event_t humidity2,temp2;
  temperature_sensors[1]->getEvent(&humidity, &temp);
  temperature_sensors[2]->getEvent(&humidity2, &temp2);
  float_matrix[1] = temp.temperature;
  float_matrix[2] = temp2.temperature;
  Serial.println(float_matrix[1]);
  Serial.println(float_matrix[2]);

  Serial.println("capteur 2");
  mux70.setPort(3);
  temperature_sensors[3]->getEvent(&humidity, &temp);
  float_matrix[3] = temp.temperature;
  Serial.println(float_matrix[3]);
  
  Serial.println("capteur 3");
  mux70.setPort(4);
  sensors_event_t humidity71_3,temp71_3;
  temperature_sensors[4]->getEvent(&humidity71_3, &temp71_3);
  temperature_sensors[5]->getEvent(&humidity, &temp);
  float_matrix[4] = temp71_3.temperature;
  float_matrix[5] = temp.temperature;
  Serial.println(float_matrix[4]);
  Serial.println(float_matrix[5]);
  
  Serial.println();
  delay(5000);
}

void receiveData(){
  j =j++;
  Serial.println("receiveData");
  Serial.println(j);
}

void sendData(){
  Serial.println(float_matrix[j]);
  dtostrf(float_matrix[j],7,2,data);
  Wire.write(data);
}
