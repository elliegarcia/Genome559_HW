import sys
import random
import math

position = 0
steplist = [0]
for step in range(0,int(sys.argv[1])-1):
    randint = random.random()
    if randint > 0.5:
        position += 1
    else:
        position -= 1
    steplist.append(position)
print steplist

for item in steplist:
    valuetocompare = math.fabs(item)
    if valuetocompare > item:
        print valuetocompare
    else:
        print item