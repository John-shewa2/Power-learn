class Superhero:
    def __init__(self, name, power, villain):
        self.name = name
        self.power = power
        self.villain = villain

    def display_info(self):
        return f"Superhero Name: {self.name}, Power: {self.power}, Villain: {self.villain}"


Spider_man = Superhero("Spider-Man", "Wall-Crawling", "Green Goblin")
Super_man = Superhero("Superman", "Super Strength", "Lex Luthor")
print(Spider_man.display_info())
print(Super_man.display_info())

# Inheritance and Polymorphism


class Animal:
    def __init__(self, animal, movement_type="walk"):
        self.name = animal
        self.movement_type = movement_type


class Dog(Animal):
    def display_info(self):
        self.movement_type = "run"
        return f"A dog {self.movement_type}s."


class Shark(Animal):
    def display_info(self):
        self.movement_type = "swim"
        return f"A shark {self.movement_type}s."


class Eagle(Animal):
    def display_info(self):
        self.movement_type = "fly"
        return f"An eagle {self.movement_type}s."


print(Dog("Dog").display_info())
print(Shark("Shark").display_info())
print(Eagle("Eagle").display_info())
