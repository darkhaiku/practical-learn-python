import sys
sys.stdout = open('practical-learn-python', 'w')

class Car:
    def __init__(self, make, model) -> None:
        self.make = make 
        self.model = model 

    def __str__(self):
        return f'Car: {self.make}, {self.model}'

    def __repr__(self) -> str:
        return f'Car: {self.make}, {self.model}'

my_car = Car('Ford', 'Thunderbird')
print(str(my_car))
print(repr(my_car))

sys.stdout.close()