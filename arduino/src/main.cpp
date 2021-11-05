#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_HTU31D.h"
#include "Adafruit_SGP30.h"
#include "SparkFun_I2C_Mux_Arduino_Library.h"

Adafruit_HTU31D htu = Adafruit_HTU31D();
//Adafruit_SGP30 sgp = Adafruit_SGP30();
QWIICMUX myMux;

uint32_t timestamp;

void purgeMoisture(int time_delay)
{
  htu.enableHeater(true);
  delay(time_delay);
  htu.enableHeater(false);
}

void setup()
{
  Serial.begin(115200);
  Wire.begin();
  while (!Serial)
  {
    delay(10); //wait till serial port opens
  }
  if (!htu.begin(0x40))
  {
    Serial.println("Couldn't find the sensor!");
  }
  purgeMoisture(5000);
  timestamp = millis();
}

void loop()
{
  sensors_event_t humidity, temp;
  htu.getEvent(&humidity, &temp);
  //sgp.eCO2;
  //sgp.TVOC;
  Serial.println(humidity.relative_humidity);
  Serial.println(temp.temperature);
  timestamp = millis();
}