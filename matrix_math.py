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

## This function takes two matrix files, adds them together (entry-wise), and prints the result
def summatrix(matrixfile1, matrixfile2):
    matrix1 = make2dlist(matrixfile1) # turns the matrix file into a list
    matrix2 = make2dlist(matrixfile2)
    result = matrix1 # initialize the result
    for i in range(len(matrix1)): # iterate through rows
        for j in range (len(matrix1[0])): # iterate through columns
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    pretty_result = beautifymatrix(result) # make the matrix pretty
    return pretty_result

########## Running the Functions ###########
matrixfile = open(sys.argv[1], "r")
matrixfile2p0 = open(sys.argv[1], 'r')
answer = summatrix(matrixfile, matrixfile2p0)
print answer
# https://stackoverflow.com/questions/10508021/matrix-multiplication-in-python
def matmult(a,b):
    zip_b = zip(*b)
    # uncomment next line if python 3 :
    # zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]

x = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
y = [[1,2],[1,2],[3,4]]