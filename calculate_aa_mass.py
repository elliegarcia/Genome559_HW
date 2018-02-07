import sys
massesfile = open(sys.argv[2],"r")
aminoacidfile = open(sys.argv[3], "r")
for amino in range(0,20):
    massesline = massesfile.readline()
    masseslist = massesline.split()
    print masseslist