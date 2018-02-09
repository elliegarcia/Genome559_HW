import sys
chromosome21file = open(sys.argv[1], "r") # opens the chromosome document
chromosome21string = chromosome21file.read() # turn the chromosome document into a string
chromosome21string = chromosome21string.upper() # make all the letters uppercase
chromosome21string = chromosome21string.replace('\n', '') # get rid of \n in the string
chromosome21string = chromosome21string.replace('\r', '')

endpoint = len(chromosome21string) - int(sys.argv[2]) # endpoint to keep the magnifier from running off
countsdictionary = {} # make a dictionary
counts = 0 # start a counter
for line in chromosome21string:
    endmag = counts + int(sys.argv[2]) # make the end of the magnifier
    magnifier = chromosome21string[counts:endmag] # define the magnifier
    counts += 1 # increment the count by one to move the magnifier forward
    if (counts > endpoint): # break the loop if the magnifier does not fit
        break
    if (magnifier in countsdictionary): # search for the magnifier in the dictionary
        countsdictionary[magnifier] += 1
    else:
        countsdictionary[magnifier] = int(1)

countskeys = countsdictionary.keys() # make a variable with just the keys
countskeys.sort() # sort the keys
for key in countskeys:
    print key + "\t" + str(countsdictionary[key])
chromosome21file.close()