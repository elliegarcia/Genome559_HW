import sys
import random
import math
## This function simulates an M-step random walk, starting at 0,
## and returns the absolute value of the maximum deviation
def findmaxdev(steps):
    position = int(0) # initialize a starting point of 0
    steplist = [int(0)] # initialize a list with first item 0
    for step in range(0,int(steps-1)): # loop to add step values for each step definied
        randint = random.random() # set a random num between 0 & 1
        if randint > 0.5: # use the num to randomly increment by +1 or -1
            position += int(1) # save the increment to variable called position
        else:
            position -= int(1)
        steplist.append(position) # add the variable position to the list
    absoluteval_steplist = [] # initialize a new list
    for item in steplist: # for each item in the original list
        absoluteval_item = math.fabs(item) # find the absolute value of the item
        absoluteval_steplist.append(absoluteval_item) # save that new value to the new list
    return max(absoluteval_steplist) # return the max absolute value from the list

## This function returns the mean of a list
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

######## Running the Functions ####################
maxdeviationslist = [] # initialize a list for all the maximum deviations
for x in range(0, 100): # loop for 100 different walks
    maxdevitem = findmaxdev(int(sys.argv[1])) # find the maximum deviation of a walk of 'sys.argv[1]' steps
    maxdeviationslist.append(maxdevitem) # add that number to the list
maxmean = mean(maxdeviationslist) # find the mean of the list
print maxmean