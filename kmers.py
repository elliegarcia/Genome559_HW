import sys
chromosome21file = open(sys.argv[1], "r") #opens the chromosome document
chromosome21string = chromosome21file.read() #turn the chromosome document into a string
chromosome21string = chromosome21string.upper() #make all the letters uppercase
chromosome21string = chromosome21string.replace('\n', '') #get rid of \n in the string
countsdictionary = {} #make a dictionary
counts = 0 #start a counts
for line in chromosome21string:
    endmag = counts + int(sys.argv[2])
    magnifier = chromosome21string[counts:endmag]
    counts += 1
    if magnifier in countsdictionary:
        countsdictionary[magnifier] += 1
    else:
        countsdictionary[magnifier] = int(1)
countskeys = countsdictionary.keys()
countskeys.sort()
for key in countskeys:
    print key + "\t" + str(countsdictionary[key])
chromosome21file.close()