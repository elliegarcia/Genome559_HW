import sys
ogfile = open(sys.argv[1], "r")
ogstring = ogfile.readlines()
oglist = list(ogstring)
oglist.reverse()
print oglist