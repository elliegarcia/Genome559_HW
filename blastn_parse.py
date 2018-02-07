import sys
numberoflines = sum(1 for line in open(sys.argv[1]))
blastnoutfile = open(sys.argv[1], "r")
for line in range(0,numberoflines):
    blastnoutline = blastnoutfile.readline()
    blastnoutlist = blastnoutline.split()
    if ('Score' in blastnoutlist):
        print "Score", blastnoutlist.pop(2), "bits, E-value", blastnoutlist.pop(6)
blastnoutfile.close()