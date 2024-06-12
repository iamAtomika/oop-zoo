class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return "Animal sound" #as per test assert animal.speak() == "Animal sound"
    
class Mammal (Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def give_birth(self):
        return f"{self.name} the {self.species} has given birth"
    
class Bird (Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

class Reptile (Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def bask_in_sun(self):
        return f"{self.name} the {self.species} is basking in the sun"
    
class Primate (Mammal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def climb_trees(self):
        return f"{self.name} the {self.species} is climbing trees"
    
class Marsupial (Mammal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def carry_baby(self):
        return f"{self.name} the {self.species} is carrying its baby"
    
class Aviary:
    def __init__(self, birds=None):
        self.birds = [] 

    def add_birds(self, bird):
        self.birds.append(bird)

class ReptileEnclosure:
    def __init__(self, reptiles=None):
        self.reptiles = [] 

    def add_reptiles(self, reptile):
        self.reptiles.append(reptile)


# #instances
# leo = Mammal("Leo", "Lion")
# polly = Bird("Polly", "Parrot", "20 inches")
# rex = Reptile("Rex", "Iguana")
# george = Primate("George", "Chimpanzee")
# joey = Marsupial("Joey", "Kangaroo")

# #methods
# print(leo.speak())
# print(leo.give_birth())
# print(polly.speak())
# print(f"{polly.name} the {polly.species} has a wingspan of {polly.wingspan}")
# print(rex.speak())
# print(rex.bask_in_sun())
# print(george.speak())
# print(george.climb_trees())
# print(joey.speak())
# print(joey.carry_baby())

# #creating enclosures
# reptile_enclosure = ReptileEnclosure()
# aviary_enclosure = Aviary()

# #adding reptiles and birds
# reptile_enclosure.add_reptiles(rex)
# aviary_enclosure.add_birds(polly)

# print(reptile_enclosure)
# print(aviary_enclosure)