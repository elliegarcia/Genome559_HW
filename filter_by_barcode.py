import sys
barcodesfile = open(sys.argv[3], "r") #opens the barcodes.txt document
barcodesstring = barcodesfile.read()
for line in barcodesstring:
    print line

#barcodeslist = barcodesstring.split()
#barcodesindex = barcodeslist.index(sys.argv[1])
#readsfile = open(sys.argv[2], "r")
#readstring = readsfile.read()
#readslist = readstring.split()
#finalread = readslist.pop(barcodesindex)
#print finalread