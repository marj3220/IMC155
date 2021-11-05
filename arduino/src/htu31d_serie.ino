#include <Wire.h>
#include "Adafruit_HTU31D.h"

Adafruit_HTU31D htu_1 = Adafruit_HTU31D();
Adafruit_HTU31D htu_2 = Adafruit_HTU31D();

void setup() {
  Serial.begin(115200);
  while (!Serial) {
    delay(100); // wait till serial port opens
  }
  Serial.println("Adafruit HTU31D test");

  if (!htu_1.begin(0x40) || !htu_2.begin(0x41)) {
    Serial.println("Couldn't find sensor!");
    while (1);
  }
}

void loop() {
  sensors_event_t humidity_1, temp_1;
  sensors_event_t humidity_2, temp_2;
  
  htu_1.getEvent(&humidity_1, &temp_1);// populate temp and humidity objects with fresh data
  htu_2.getEvent(&humidity_2, &temp_2);// populate temp and humidity objects with fresh data

  Serial.println("Capteur 0x40");
  Serial.print("Temp: "); 
  Serial.print(temp_1.temperature);
  Serial.println(" C");
  Serial.print("Humidity: ");
  Serial.print(humidity_1.relative_humidity);
  Serial.println(" \% RH");
  Serial.println("");

  Serial.println("Capteur 0x41");
  Serial.print("Temp: "); 
  Serial.print(temp_2.temperature);
  Serial.println(" C");
  Serial.print("Humidity: ");
  Serial.print(humidity_2.relative_humidity);
  Serial.println(" \% RH");
  Serial.println("_______");

  delay(5000);
}
