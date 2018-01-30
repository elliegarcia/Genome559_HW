import sys
#total = 0
#for num in sys.argv[1:]:
#    integernum = int(num)
#    total = total + integernum
#    print total

#maxnum = int(sys.argv[1])
#total = 0
#square = 0
#while ( total < maxnum):
#    square = square + 1
#    total = square * square
#    print total

myfile = open(sys.argv[1], "r")
linecount = 0
line = myfile.readline()
while (line != ""):
    linecount += 1
    line = myfile.readline()
    print linecount