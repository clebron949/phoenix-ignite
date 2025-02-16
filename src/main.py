import platform
from datetime import datetime
from sensor import Sensor
from smtp import SMTP

EMAIL = 'christopher.lebron1@gmail.com'
TESTER_NAME = platform.node()

sensor = Sensor(port='COM3', baudrate=9600, timeout=1)
smtp = SMTP()

print('Performing test...')

sensor.read()

if(sensor.power > 2.5 and sensor.power < 3.5):
    status = 'Pass'
else:
    status = 'Fail'

body = f"""
Test Summary

Date: {datetime.now():%Y-%m-%d %H:%M:%S}
Part Number: LED
Serial Number: 123456
Tester: {TESTER_NAME}
Operator: Chris Lebron
Test Description: Test the LED power consumption.

Test Results

Voltage: {sensor.voltage}V
Current: {sensor.current}A
Power: {sensor.power}W
Status: {status}
"""

print(body)
print(f"Sending results to {EMAIL}...")

smtp.send(EMAIL, 'Test is complete!', body)

print(f"Sending results to {EMAIL}... Complete!")
print('Performing test... Complete!')
