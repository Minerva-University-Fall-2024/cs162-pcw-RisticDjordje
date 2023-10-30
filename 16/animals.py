class Animal:
    HERBIVORE = "herbivore"
    CARNIVORE = "carnivore"
    OMNIVORE = "omnivore"

    def __init__(self, name, weight, age, diet_type):
        self.name = name
        self.weight = weight
        self.age = age
        self.diet_type = diet_type

    def feed(self, food):
        if (self.diet_type == self.HERBIVORE and "meat" in food) or \
           (self.diet_type == self.CARNIVORE and "plant" in food):
            print(f"Cannot feed {food} to {self.name}, it's not suitable for a {self.diet_type}.")# noqa 
        else:
            print(f"{self.name} has been fed {food}.")

    def __repr__(self):
        return f"Animal({self.name}, {self.weight}, {self.age}, {self.diet_type})"# noqa
    

class Enclosure:
    def __init__(self, name, temperature_range):
        self.name = name
        self.temperature_range = temperature_range
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_animals(self):
        for animal in self.animals:
            print(f"{animal.name} is in the {self.name} enclosure.")


class Zoo:
    def __init__(self):
        self.enclosures = []

    def add_enclosure(self, enclosure):
        self.enclosures.append(enclosure)

    def show_zoo_animals(self):
        for enclosure in self.enclosures:
            enclosure.show_animals()


# Inheriting from the Animal class
class Lion(Animal):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age, Animal.CARNIVORE)


class Giraffe(Animal):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age, Animal.HERBIVORE)


class Shark(Animal):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age, Animal.CARNIVORE)


class Bear(Animal):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age, Animal.OMNIVORE)


class Parrot(Animal):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age, Animal.HERBIVORE)


class Tiger(Animal):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age, Animal.CARNIVORE)


# Initialize the zoo
my_zoo = Zoo()

# Create enclosures
savannah = Enclosure("Savannah", (25, 31))
aquarium = Enclosure("Aquarium", (17, 18))
forest = Enclosure("Forest", (20, 25))
aviary = Enclosure("Aviary", (18, 22))

# Add enclosures to the zoo
my_zoo.add_enclosure(savannah)
my_zoo.add_enclosure(aquarium)
my_zoo.add_enclosure(forest)
my_zoo.add_enclosure(aviary)


# Create some animals
leo = Lion("Leo", 190, 5)
zara = Giraffe("Zara", 800, 7)
sammy = Shark("Sammy", 250, 3)
baloo = Bear("Baloo", 400, 10)
rio = Parrot("Rio", 0.5, 2)
stripes = Tiger("Stripes", 250, 4)


# Add animals to their enclosures
savannah.add_animal(leo)
savannah.add_animal(zara)
aquarium.add_animal(sammy)
forest.add_animal(baloo)
forest.add_animal(stripes)
aviary.add_animal(rio)

# Show animals in the zoo
my_zoo.show_zoo_animals()


# Feed the animals
leo.feed("steak")
zara.feed("leaves")
sammy.feed("fish")
baloo.feed("fish")
rio.feed("seeds")
stripes.feed("chicken")


my_zoo.show_zoo_animals()