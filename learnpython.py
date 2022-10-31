import sys
sys.stdout = open('practical-learn-python', 'w')


class Car:
    runs = True
    number_of_wheels = 4

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels

        

    def start(self):
        if self.runs:
            print('Car is started.Vroom!Vroom!')
        else:
            print("Car is broken!")

my_car = Car()
print(my_car.number_of_wheels)
print(my_car.get_number_of_wheels())

my_car.number_of_wheels = 6
print(my_car.number_of_wheels)
print(my_car.get_number_of_wheels())

sys.stdout.close()

