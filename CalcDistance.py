import math
## This function calculates the Euclidean distance between 2 points
def CalcDistance(listA, listB):
    squared = [] # initialize the list of squared numbers
    for item in listA: # for each item in the first list
        item2 = listB.pop(0) # pop the first item in the second list
        if item < 0 and item2 < 0: # if both numbers are negative
            summeditems = math.fabs(item) - math.fabs(item2) # subtract one from the other
            summeditems = math.fabs(summeditems) # take the absolute value of the subtraction
        elif item < 0: # if 1 number is negative
            summeditems = math.fabs(item) + math.fabs(item2) # add the absolute value of both numbers
        elif item2 < 0: # if 1 number is negative
            summeditems = math.fabs(item) + math.fabs(item2) # add the absolute value of both numbers
        else: # if both numbers are positive
            summeditems = math.fabs(item) - math.fabs(item2) # subtract one from the other
            summeditems = math.fabs(summeditems) # take the absolute value of the subtraction
        squaredsum = math.pow(summeditems, 2) # take the square of the answer
        squared.append(squaredsum) # add it to the list of squared numbers

    newitem = 0 # initialize the new item
    for item in squared: # for each item in the list of squared numbers
        newitem = item + newitem # add them to the item before
    euclidian_dist = math.sqrt(newitem) # take the square root of the final answer
    return euclidian_dist # return that number
######## Running the Function ######
listA = [-7, -5, 2]
listB = [17, 7, 3.5]
print CalcDistance(listA, listB)