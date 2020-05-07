import smbus
import time
import random

bus = smbus.SMBus(1)
bus.read_byte_data(0x39, 0x00 | 0x80)
bus.read_byte_data(0x39, 0x01 | 0x80)
time.sleep(0.5)
data = bus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)

data1 = bus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)

ch0 = data[1] * 256 + data[0]
ch1 = data1[1] * 256 + data1[0]


try:
    while True:
		light = (ch0 - ch1)
		light = random.randint(0,1500)
		if (light<=50):
			print("Distance is below 50. It is too close")

		elif (light<=100):
			print("Distance is 100 or below. It is close")
				
		elif (light<=400):
			print("Distance is 400 or below. It is okay")

		elif (light<=1200):
			print("Distance is 1200 or below. It is far")
		else: 
			print("Distance is above 1200. It is too far away")
except KeyboardInterrupt:
    GPIO.cleanup()