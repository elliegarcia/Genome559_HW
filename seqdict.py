import sys
seqsfile = open(sys.argv[1], "r") # open the file
sequencedictionary = {} # set up an empty dictionary

counts = 0
animalname = []
value = []
for line in seqsfile: # making the seqs.txt into a dictionary line by line
    if counts %2 == 0: # turn even numbered lines into keys
        animalname = line.strip()
        animalname = "".join(animalname)
    else: # turn odd numbered lines into values
        value = line.strip()
        sequencedictionary[animalname] = value # put everything into a dictionary
    counts += 1 # add the count to continue moving down a line

if sys.argv[2] in sequencedictionary: # what to print based on the query
    print sys.argv[2]
    print sequencedictionary[sys.argv[2]]
else:
    print "sequence", sys.argv[2], "not found"
seqsfile.close()