class Animal:
    
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        return f"{self.name} the {self.species} says {self.sound}!"

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."


class Cow(Animal):
    
    def __init__(self, name):
        super().__init__(name, "Cow", "Moo")

    def produce_milk(self):
        return f"{self.name} is producing milk."


class Chicken(Animal):
    
    def __init__(self, name):
        super().__init__(name, "Chicken", "Cluck")

    def lay_egg(self):
        return f"{self.name} laid an egg."


class Horse(Animal):
    
    def __init__(self, name):
        super().__init__(name, "Horse", "Neigh")

    def gallop(self):
        return f"{self.name} is galloping."


cow = Cow("Bessie")
chicken = Chicken("Clucky")
horse = Horse("Thunder")

print(cow.make_sound())  
print(cow.produce_milk())  
print(chicken.make_sound())  
print(chicken.lay_egg())    
print(horse.make_sound())   
print(horse.gallop())        