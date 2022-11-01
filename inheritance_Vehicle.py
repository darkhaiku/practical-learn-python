
class Vehicle:
    def __init__(self, make, model, fuel = 'gas') -> None:
        self.make = make 
        self.model = model 
        self.fuel = fuel 


# we call super().__init__(), which resolves to our parent class,
#  Vehicle, and runs its __init__ function,
#  where the variables are stored.

class Car(Vehicle):
    def __init__(self, make, model, fuel='gas') -> None:
        super().__init__(make, model, fuel)