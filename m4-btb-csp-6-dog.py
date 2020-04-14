# demonstrates: class declaration, subclassing
# class declaration
class Dog(object):
    # declarations
    name = ""
    age = 0
    breed = ""
    weight = 0.0
    height = 0.0
    color = ""

    # demonstrates: __init__ declaration, context, override
    # constructor
    def __init__(self, name, age, breed, weight, height, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.weight = weight
        self.height = height
        self.color = color

    # setter/getter
    def setWeight(self, weight):
        self.weight = weight

    def getWeight(self):
        return self.weight

    # methods
    def walk(self):
        print(self.name + " goes for a walk.")

    def bark(self):
        print(self.name + " barks.")

    # str override
    def __str__(self):
        return str(self.age) + " year old " + str(self.weight) + "lb, " + str(self.height) + " foot tall " + self.color + " " + self.breed + " named " + self.name + "."

# script
# instantiate
penny = Dog("Penny", 6, "Red Heeler", 20, 1.5, "Brown")
# describe
print(penny)
# walk
penny.walk()
# bark
penny.bark()