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

sequence = []
length = len(greenlist)
for base in range(0,length):
    if (redlist[base] > greenlist[base]) and (redlist[base] > bluelist[base]) and (redlist[base] > yellowlist[base]):
        sequence.append("T")
    elif (greenlist[base] > redlist[base]) and (greenlist[base] > bluelist[base]) and (greenlist[base] > yellowlist[base]):
        sequence.append("A")
    elif (bluelist[base] > redlist[base]) and (bluelist[base] > greenlist[base]) and (bluelist[base] > yellowlist[base]):
        sequence.append("C")
    elif (yellowlist[base] > redlist[base]) and (yellowlist[base] > greenlist[base]) and (yellowlist[base] > bluelist[base]):
        sequence.append("G")
sequence = "".join(sequence)
print sequence

greenfile.close()
redfile.close()
bluefile.close()
yellowfile.close()