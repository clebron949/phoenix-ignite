import serial

class Sensor:
    def __init__(self, port, baudrate, timeout):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout

    def read(self):
        response = False
        self.ser = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
        self.ser.flush()
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        while not response:
            if self.ser.in_waiting > 0:
                data = self.ser.readline().decode().strip()
                measurements = data.split(',')
                self.voltage = float(measurements[0])
                self.current = float(measurements[1])
                self.power = float(measurements[2])
                response = True
        self.ser.close()
