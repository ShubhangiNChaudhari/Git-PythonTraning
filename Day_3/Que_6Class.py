class Car:
	x = 'car'
	def __init__(self, brand, color):

		# Instance Variable
		self.brand = brand
		self.color = color

Verna = Car("Verna", "white")
harrier= Car("Harrier", "black")

print('Verna details:')
print('My love is a', Verna.x)
print('Brand: ', Verna.brand)
print('Color: ', Verna.color)

print('\nHarrier details:')
print('My love is a', harrier.x)
print('Brand: ', harrier.brand)
print('Color: ', harrier.color)

print("\nAccessing class variable using class name")
print(Car.x)
