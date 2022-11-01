import sys
sys.stdout = open('practical-learn-python', 'w')

from inheritance_vehicle_2 import Truck

my_truck = Truck('Ford', 'F350')
print('my_truck type: ')
print(type(my_truck))
print('--- --- ---')
print('my_truck uses: ')
print(my_truck.fuel)
print('--- --- ---')
print('my_truck wheels')
print(my_truck.number_of_wheels)

sys.stdout.close()
