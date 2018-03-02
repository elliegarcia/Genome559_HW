import sys
import random

class Dice:
    def __init__(self, numDice, numSides):
        self.numDice = int(numDice)
        self.numSides = numSides
    def Roll(self):
        random.randint(0, numSides):
        
    def __str__(self):
        numDice_str = '%s' % self.numDice
        numSides_str = '%s' % self.numSides
        return '[' + numDice_str + ',' + numSides_str + ']'

Craps_dice = Dice (2, 6)
print Craps_dice