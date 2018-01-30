import sys
seqfile = open(sys.argv[1], "r")
seqstring = seqfile.read()
if ('-' in seqstring):
    missingbasescount = seqstring.count("-")
    print missingbasescount, "missing bases detected."
else:
    print "No missing bases detected."
seqfile.close()