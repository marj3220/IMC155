#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_HTU31D.h"
#include "Adafruit_SGP30.h"
#include "SparkFun_I2C_Mux_Arduino_Library.h"

#define NUMBER_OF_TEMP_SENS 4
//Adafruit_SGP30 sgp = Adafruit_SGP30();
QWIICMUX myMux;
uint32_t timestamp;

Adafruit_HTU31D **temperature_sensors;

void purgeMoisture(int time_delay)
{
  for (byte i = 0; i < NUMBER_OF_TEMP_SENS; i = i + 2)
  {
    myMux.setPort(i);
    for (byte j = 0; j < 2; j++)
    {
      temperature_sensors[i + j]->enableHeater(true);
    }
  }
  delay(time_delay);
}

void setup()
{
  Serial.begin(115200);
  Wire.begin();
  temperature_sensors = new Adafruit_HTU31D *[NUMBER_OF_TEMP_SENS];
  for (int x = 0; x < NUMBER_OF_TEMP_SENS; x++)
  {
    temperature_sensors[x] = new Adafruit_HTU31D();
  }
  if (myMux.begin() == false)
  {
    Serial.println("Mux not detected. Freezing...");
    while (1)
      ;
  }
  byte i = 0;
  for (byte x = 0; x < NUMBER_OF_TEMP_SENS; x = x + 2)
  {
    myMux.setPort(i);
    if (!temperature_sensors[x]->begin(0x40) || !temperature_sensors[x + 1]->begin(0x41))
    {
      Serial.println("Couldn't find sensor!");
      while (1)
        ;
    }
    i++;
  }
  purgeMoisture(5000);
}

void loop()
{
  for (byte i = 0; i < NUMBER_OF_TEMP_SENS / 2; i++)
  {
    myMux.setPort(i);
    for (byte j = 0; j < 2; j++)
    {
      sensors_event_t humidity, temp;
      temperature_sensors[i + j]->getEvent(&humidity, &temp);
      Serial.print("Sensor ");
      Serial.print(i);
      Serial.print(" Id ");
      Serial.print(j);
      Serial.println();
      Serial.println(humidity.relative_humidity);
      Serial.println(temp.temperature);
      Serial.println();
    }
  }
  delay(2000);
}