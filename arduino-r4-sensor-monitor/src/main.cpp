#include <Arduino.h>

float GetVoltage();
float GetCurrent();

const int voltagePin = A0;
const int currentPin = A2;
const int samples = 20;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  float voltageSum = 0;
  float currentSum = 0;

  for (int i = 0; i < samples; i++)
  {
    voltageSum += GetVoltage();
    currentSum += GetCurrent();
    delay(250);
  }

  float voltageAverage = voltageSum / samples;
  float currentAverage = currentSum / samples;

  String message = String(voltageAverage) + "," + String(currentAverage) + "," + String(voltageAverage * currentAverage);
  Serial.println(message);
}

float GetVoltage()
{
  float voltageGain = 5;
  int voltageSensorValue = analogRead(voltagePin);
  float voltage = voltageSensorValue * (5 / 1023.0) * voltageGain;
  return voltage;
}

float GetCurrent()
{
  float sensitivity = 0.4; // v/A
  float offset = 2.5;      // v
  int currentSensorValue = analogRead(currentPin);
  float rawCurrent = currentSensorValue * (5.0 / 1023.0);
  float current = (rawCurrent - offset) / sensitivity;
  return current;
}