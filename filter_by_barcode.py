import sys
query = sys.argv[1]
barcodesfile = open(sys.argv[3], "r") #opens the barcodes.txt document
readsfile = open(sys.argv[2]) #opens the reads.txt document
for line in readsfile: #made a for loop with the reads file setting the number of iterations
    barcodesstring = barcodesfile.readline() #read each consecutive line of the barcodes file
    if query in barcodesstring: #if the query matches the line in the barcodes file
        print line #prints the corresponding reads line
barcodesfile.close()
readsfile.close()