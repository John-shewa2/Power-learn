class car:
    def __init__(self, model):
        self.model = model

    def wheel(self):
        print("The car has 4 wheels.")


class electric_car(car):
    def seats(self):
        print(f"The electric car with the model {self.model} has 5 seats.")


BYD = electric_car("BYD")
BYD.wheel()
BYD.seats()
