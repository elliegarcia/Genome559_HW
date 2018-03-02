import sys
import random

class Dice:
    def __init__(self, numDice, numSides):
        self.numDice = int(numDice)
        self.numSides = int(numSides)

    def Roll(self):
        mylist = []
        for x in range(0,2):
            x = random.randint(1, 6)
            mylist.append(x)
        return mylist

    def __str__(self):
        mylist_str = '%s' % mylist
        return mylist_str

Craps_dice = Dice (2, 6)
print Craps_dice