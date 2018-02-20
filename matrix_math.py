import sys

def make2dlist(mymatrixfile):
    matrixlist = []
    for line in mymatrixfile:
        line = line.strip()
        line = line.replace('  ', ' ')
        linelist = line.split(' ')
        linelist = map(int, linelist)
        matrixlist.append(linelist)
    return matrixlist

def beautifymatrix(matrixlist):
    stringline = ''
    for line in matrixlist:
        stringline2 = '  '.join(map(str, line))
        stringline2 = stringline2 + '\n'
        stringline = stringline + stringline2
    stringline.strip()
    return stringline

matrixfile = open(sys.argv[1], "r")
listoflists = make2dlist(matrixfile)
matrixfile2 = open(sys.argv[1], 'r')
listoflists2 = make2dlist(matrixfile2)

for item in listoflists:
    print item