import sys
firstfastafile = open(sys.argv[1], "r")
firstfastastring = firstfastafile.readlines()
secondfastafile = open(sys.argv[2], "r")
secondfastastring = secondfastafile.readlines()
concatenatedfasta = firstfastastring + secondfastastring

newfile = open(sys.argv[3], "w")
newfile.write("%s"%concatenatedfasta)
newfile.close()
firstfastafile.close()
secondfastafile.close()
print "Fasta concatenation complete!"