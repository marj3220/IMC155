#include <Wire.h>
#include "Adafruit_HTU31D.h"
#include "Adafruit_SGP30.h"
#include "SparkFun_I2C_Mux_Arduino_Library.h"

#define SLAVE_ADDRESS 0x08

Adafruit_HTU31D **temperature_sensors;
QWIICMUX myMux;

const int nb_sensors = 4;
float float_matrix[nb_sensors] = {0};
char data[7];
int j = 99;

void setup() 
{
  Wire.begin(SLAVE_ADDRESS);
  Serial.begin(115200);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);

  while (!Serial) {
    delay(100); // wait till serial port opens
  }

  temperature_sensors = new Adafruit_HTU31D *[nb_sensors];
  for (int x=0 ; x<nb_sensors ; x++){
    temperature_sensors[x] = new Adafruit_HTU31D();
  }

  if (myMux.begin() == false){
    Serial.println("Mux not detected. Freezing...");
    while (1)
      ;
  }
  Serial.println("Mux detected");

  byte i = 0;
  for (byte x = 0; x < nb_sensors; x = x + 2){
    myMux.setPort(i);
    if (!temperature_sensors[x]->begin(0x40) || !temperature_sensors[x + 1]->begin(0x41)){
      Serial.println("Couldn't find sensor!");
      while (1)
        ;
    }
    i++;
  }
  purgeMoisture(5000);
}

void loop(){
  byte k = 0;
  for (byte i = 0; i < nb_sensors/2; i++){
    myMux.setPort(i);
    for (byte j = 0; j < 2; j++){
      sensors_event_t humidity, temp;
      temperature_sensors[k + j]->getEvent(&humidity, &temp);
      float_matrix[k+j] = temp.temperature;
      Serial.println(float_matrix[k+j]);
    }//
    k = k + 2;
  }
  delay(5000);
}
  

void purgeMoisture(int time_delay){
  for (byte i = 0; i < nb_sensors; i = i + 2){
    myMux.setPort(i);
    for (byte j = 0; j < 2; j++){
      temperature_sensors[i + j]->enableHeater(true);
    }
  }
  delay(time_delay);
}

void receiveData(){
  j = Wire.read();
  Serial.println("receiveData");
  Serial.println(j);
}

void sendData(){
  Serial.println(float_matrix[j]);
  dtostrf(float_matrix[j],7,2,data);
  Wire.write(data);
}
