import sys
sys.stdout = open('practical-learn-python', 'w')

class Car:
    runs = True

    def __init__(self, make, model) -> None:
        self.make = make 
        self.model = model 

    def start(self):
        if self.runs:
            print(f"your {self.make} {self.model} is started. Vroom Vroom!")

        else:
            print(f"your {self.make} {self.model} is broken!")

my_car = Car('Ford', 'Thunderbird')
my_car.start()

sys.stdout.close()

