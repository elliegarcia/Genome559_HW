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

## This function takes a 2D list of integers and prints it in a pretty format
def beautifymatrix(matrixlist):
    stringline = '' # initialize a string
    for line in matrixlist: # for each list in the bigger list
        stringline2 = '  '.join(map(str, line)) # turn the list into a string
        stringline2 = stringline2 + '\n' # add a return to the string
        stringline = stringline + stringline2 # concatonate the line with the one before
    stringline.strip() # strip the string
    return stringline

## This function takes 2 matrix files, adds them together (entry-wise), and prints the result
def summatrix(matrixfile1, matrixfile2):
    matrix1 = make2dlist(matrixfile1) # turn the matrix file into a list
    matrix2 = make2dlist(matrixfile2)
    result = matrix1 # initialize the result
    for i in range(len(matrix1)): # iterate through rows
        for j in range (len(matrix1[0])): # iterate through columns
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    pretty_result = beautifymatrix(result) # make the matrix pretty
    return pretty_result

## This Function takes 2 matrix files, multiplies them, and prints the result
def multiplymatrix(matrixfileA, matrixfileB):
    matrixA = make2dlist(matrixfileA) # turn the matrix files into lists
    matrixB = make2dlist(matrixfileB)
    matrixC = [[0 for row in range(len(matrixB[0]))] for col in range(len(matrixA))] # initialize the result
    for i in range(len(matrixA)): # iterate through the rows of matrix A
        for j in range(len(matrixB[0])): # iterate through the columns of matrix B
            for k in range(len(matrixA[0])): # iterate through columns of matrix A
                matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
    pretty_matrixC = beautifymatrix(matrixC)
    return pretty_matrixC

########## Running the Functions ###########
import sys
matrixfile = open(sys.argv[1], "r")
matrixfile2 = open(sys.argv[2], 'r')
print summatrix(matrixfile, matrixfile2)

matrixfile = open(sys.argv[1], "r") # these are different files from the ones above
matrixfile2 = open(sys.argv[2], 'r')
print multiplymatrix(matrixfile, matrixfile2)