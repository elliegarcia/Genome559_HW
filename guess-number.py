import sys
from random import *
myrandomnumber = randint(1,10)
yournumber = int(sys.argv[1])
if (myrandomnumber < yournumber):
    print "The number I'm thinking of is less than", sys.argv[1], "."
elif (myrandomnumber > yournumber):
    print "The number I'm thinking of is more than", sys.argv[1], "."
else:
    print "The number I'm thinking of is the same as", sys.argv[1], "."