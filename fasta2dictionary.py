import sys
fastafile = open(sys.argv[1], "r") # open the file with all the information
#fastastring = fastafile.read()
#fastastring = fastastring.replace('\n', '')
#fastastring = fastastring.replace('\r', '')
fastadictionary = {} # make a dictionary to hold the sequences as values

key = "" # initialize the keys in the dictionary
value = "" # initialize the values in the dictionary
newvalue = ""
for line in fastafile: # make the dictionary
    if ">" in line: # search for lines with sp
        key = line.split(' ')# make the line the string key
        key = key[0]
        value = ""
    else:
        value = line.strip() # strip the line and call it a value
        #value = "".join(value) # turn the value into a string
        newvalue += value # concatonate value string
        fastadictionary[key] = newvalue # add keys and values to the dictionary
print fastadictionary
#ogfastafile = sys.arv[1]
#fastadict = fasta2dictionary(ogfastafile)