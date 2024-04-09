import board
import busio
import adafruit_sht31d

device_address1 = (0x45)
device_address2 = (0x44)

i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)  # Dev
sensor1 = adafruit_sht31d.SHT31D(i2c, device_address1)
sensor2 = adafruit_sht31d.SHT31D(i2c, device_address2)


class TEMP:
    def __init__(self):
        pass

    def temp1(self):
        temp = sensor1.temperature
        temp = temp * 9 / 5 + 32
        temp = temp + 1.31
        temp = round(temp, 1)
        temp = float(temp)
        return str(temp)

    def hum1(self):
        hum = sensor1.relative_humidity
        hum = round(hum)
        return str(hum)

    def temp2(self):
        temp = sensor2.temperature
        temp = temp * 9 / 5 + 32
        temp = temp + 1.31
        temp = round(temp, 1)
        temp = float(temp)
        return str(temp)

    def hum2(self):
        hum = sensor2.relative_humidity
        hum = round(hum)
        return str(hum)



temp = TEMP()
