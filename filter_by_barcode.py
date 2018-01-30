import sys
barcodesfile = open(sys.argv[3], "r") #opens the barcodes.txt document
for line in barcodesfile:
    barcodesstring = barcodesfile.readline()
    print barcodesstring

#barcodeslist = barcodesstring.split()
#barcodesindex = barcodeslist.index(sys.argv[1])
#readsfile = open(sys.argv[2], "r")
#readstring = readsfile.read()
#readslist = readstring.split()
#finalread = readslist.pop(barcodesindex)
#print finalread