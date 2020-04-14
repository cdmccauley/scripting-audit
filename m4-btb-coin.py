# imports
import random

# class definition
class Coin(object):
    # properties
    heads = True

    # constructor
    def __init__(self):
        self.heads = True

    # methods
    def flip(self):
        self.heads = random.choice([True, False])

    # overrides
    def __str__(self):
        if(self.heads):
            return "Heads"
        else:
            return "Tails"

# script
# declarations
quarter = Coin()

# flip coin and print
for i in range(0, 20):
    quarter.flip()
    print(quarter)