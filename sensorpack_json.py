# A test script for reading input of sensors BME280 and ICM20948

import board
import time
from json import dump
import adafruit_icm20x
from adafruit_bme280 import basic as adafruit_bme280

i2c = board.I2C()  # uses board.SCL and board.SDA
icm = adafruit_icm20x.ICM20948(i2c)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
bme280.sea_level_pressure = 1013.25

def readSensorData():
    
    sensordata = {"bosch_sensor":[ {
    "Acceleration": icm.acceleration, "Gyro": icm.gyro, "Magnetometer": icm.magnetic, "Temperature": bme280.temperature, 
    "Humidity":bme280.relative_humidity, "Pressure": bme280.pressure, "Altitude": bme280.altitude} ]
}
    #y = json.dumps(x)
    #json_str = json.dumps(x)
    #print(json_str)
    #json_object = json.dumps(x, indent = 7)
    with open('/claviate/data/meta_data.json', 'w') as outfile:
        #outfile.write(json_object)
        json_string = dump(sensordata, outfile)


while True:
    print("Reading sensordata..")
    readSensorData()
    time.sleep(5)
