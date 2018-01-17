import sys
startrange = int(sys.argv[2]) - 1
endrange = int(sys.argv[3])
outputvariable = sys.argv[1]
print outputvariable[startrange:endrange]