import sys
if ((sys.argv[2] == 'integer') or (sys.argv[2] == 'Integer')):
    integernum = float(sys.argv[1])
    print "%d" %integernum
elif ((sys.argv[2] == 'real') or (sys.argv[2] == 'Real')):
    realnum = float(sys.argv[1])
    print "%f" %realnum
elif ((sys.argv[2] == 'scientific') or (sys.argv[2] == 'Scientific')):
    scientificnum = float(sys.argv[1])
    print "%e" %scientificnum
else:
    print "Invalid format:", sys.argv[2]