import sys
greenfile = open(sys.argv[1], "r")
greenstring = greenfile.read()
greenlist = greenstring.split(",")
greenlist = map(int, greenlist)

redfile = open(sys.argv[2], "r")
redstring = redfile.read()
redlist = redstring.split(",")
redlist = map(int, redlist)

bluefile = open(sys.argv[3], "r")
bluestring = bluefile.read()
bluelist = bluestring.split(",")
bluelist = map(int, bluelist)

yellowfile = open(sys.argv[4], "r")
yellowstring = yellowfile.read()
yellowlist = yellowstring.split(",")
yellowlist = map(int, yellowlist)

length = len(greenlist)
for base in range(0,7):
    if (redlist.pop(base) > greenlist.pop(base)) or (redlist.pop(base) > yellowlist.pop(base)) or (redlist.pop(base) > bluelist.pop(base)):
        print "yes"
    else:
        print "no"