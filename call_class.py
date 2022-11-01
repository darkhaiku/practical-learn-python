import sys
sys.stdout = open('practical-learn-python', 'w')

from inheritance_Vehicle import Vehicle, Car

my_car = Car('Ford', 'Thunderbird')
print('my_car type: ')
print(type(my_car))
print(my_car.fuel)

print('--- --- ---')
print('my car is a Car: ')
print(isinstance(my_car, Car))
print('my_car is a Vehicle: ')
print(isinstance(my_car, Vehicle))
print('Car is subclass of Vehicle: ')
print(issubclass(Car, Vehicle))

sys.stdout.close()
