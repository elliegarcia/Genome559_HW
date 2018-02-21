import sys
## This function reads in a file containing a matrix of integers and returns it as a 2D list
def make2dlist(mymatrixfile):
    matrixlist = [] # initialize the 2D list
    for line in mymatrixfile: # for each line in the file
        line = line.strip() # strip the line
        line = line.replace('  ', ' ') # take out the whitespaces
        linelist = line.split(' ') # make the string into a list of strings
        linelist = map(int, linelist) # turn the strings into numbers
        matrixlist.append(linelist) # add the list to the 2D list
    return matrixlist

## This function takes a 2-D list of integers and prints it in a pretty format
def beautifymatrix(matrixlist):
    stringline = '' # initialize a string
    for line in matrixlist: # for each list in the bigger list
        stringline2 = '  '.join(map(str, line)) # turn the list into a string
        stringline2 = stringline2 + '\n' # add a return to the string
        stringline = stringline + stringline2 # concatonate the line with the one before
    stringline.strip() # strip the string
    return stringline


def summatrix(matrix1, matrix2):
    result = matrix1
    for i in range(len(matrix1)):

########## Running the Functions ###########
matrixfile = open(sys.argv[1], "r")
listoflists = make2dlist(matrixfile)
matrixfile2 = open(sys.argv[1], 'r')
listoflists2 = make2dlist(matrixfile2)

X = [[12,7,3],
    [4,5,6],
    [7,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[3,3,3],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)

for i in range(len(X)):
    for j in range(len(X)):
        for n in range():