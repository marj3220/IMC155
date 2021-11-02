#include <Arduino.h>
#include "Adafruit_HTU31D.h"
#include "Adafruit_SGP30.h"

Adafruit_HTU31D htu = Adafruit_HTU31D();
//Adafruit_SGP30 sgp = Adafruit_SGP30();
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
  timestamp = millis();
}