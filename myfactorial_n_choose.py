## This function calculates and returns the factorial of n
def my_factorial(n):
    count = 1 # initialize a count
    if n <0:
        print "Cannot take the factorial of a negative number"
    else:
        for i in range (1, n+1): # for every integer in 1 to n+1
            count = count*i # multiply the count by the integer and call it the new count
    return count # return the final count

## This function calculates the binomial coefficient "n choose k"
def my_choose(n, k):
    n_k = n - k # make a variable for n - k
    numerator = my_factorial(n) # define the numerator
    kfact = my_factorial(k) # define the factorial of k
    n_kfact = my_factorial(n_k) # define the factorial of n - k
    binomial = numerator/(kfact*n_kfact) # put all the variables in the formula
    return binomial # return the binomial coefficient

### Running the function ####
import sys
n = int(sys.argv[1])
k = int(sys.argv[2])

print my_factorial(n)
print my_choose(n, k)