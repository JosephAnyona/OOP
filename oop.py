class Vehicle(object):
	def __init__(self, vtype = None, yrManu = 2000):
		self.vehicle_type = vtype
		self.year_of_manufacture = yrManu
		if self.vehicle_type != 'trailer':
			self.vehicle_type = 'saloon'

class Car(Vehicle):#demonstrates class car inheriting from class Vehicle - inheritance
	__vin = 0  #demonstrates private variable that can only be accessed with class- Encapsulation

	def take_off(self):
		print ("shift to gear 1 and take off!")

	def set_vin_num(self, num):
		self.__vin = num

	def get_vin_num(self):
		return self.__vin


class Truck(Vehicle):
	__vin = 0

	def take_off(self):
		print ("shift to gear 2 and take off!")

	def set_vin_num(self, num):
		self.__vin = num

	def get_vin_num(self):
		return self.__vin

def vehicle_take_off(any_vehicle):# demonstrating polymorphism via a function
	return any_vehicle.take_off()