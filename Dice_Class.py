import sys
import random
## This class represents a set of playing dice
class Dice:
    def __init__(self, numDice, numSides):
        self.numDice = int(numDice) # the number of dice in the set
        self.numSides = int(numSides) # the number of sides of the dice

    def Roll(self): # This function returns a list of numbers that represents a roll of dice
        mylist = [] # initialize a list
        for x in range(0,self.numDice): # for every die
            x = random.randint(1, self.numSides) # roll the die based on the number of sides
            mylist.append(x) # add that number to a list
        return mylist

    def __str__(self):
        numDice_str = '%s' % self.numDice
        numSides_str = '%s' % self.numSides
        return numDice_str + "," + numSides_str

### Running the function ###
craps_dice = Dice(2, 6)
quest_dice = Dice(3, 10)
print craps_dice.Roll()
print quest_dice.Roll()