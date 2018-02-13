import sys
fastafile = open(sys.argv[1], "r") #open the fasta file and give it a name

def fasta_parse(fastafile): # this function puts the fastafile into a dictionary
    fastadictionary = {} # initialize a dictionary
    key = "a" # initialize the key variable
    value = "a" # initialize the value variable

    for line in fastafile: # loop that iterates over every line
        if ">" in line: # if it comes across a >
            key = line.split() # make that line the key variable
            key = key[0] # take the first item in the list
            value = "" # reset value to nothing
        else:
            line = line.strip() # if the line does not have >
            value = value + line # concatonate the value and the line
            fastadictionary[key] = value #input that value into the dictionary
    return fastadictionary #return the dictionary after the loop is done
yeastdictionary = fasta_parse(fastafile) # run the function and give the dictionary a variable
print "There are", len(yeastdictionary.keys()), "sequences in the fasta file."
fastafile.close()