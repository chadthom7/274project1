import time
import math
#establish the connection
import serial

class roomba:
	def __inti__(self):
		self.connection = serial.Serial('/dev/ttyUSB0', buadrate = 115200)
		time.sleep(1)
		connection.close()
		time.sleep(1)
		connection.open()

	def start(self):
		self.connection.write(chr(128))
		time.sleep(1)

	def stop(self):
		self.connection.write(chr(173))
		time.sleep(1)

	def reset(self):
		self.connection.write(chr(7))
		time.sleep(1)

	def safe(self):
		self.connection.write(chr(131))
		time.sleep(1)

	def state(self):


	def drive(self):
		

	def close(self):
		self.connection.close()
		time.sleep(1)
