import sys
ogfile = open(sys.argv[1], "r")
ogstring = ogfile.readlines()
newfile = open(sys.argv[2], "w")
newfile.write(%fogstring\n%)
newfile.close()
print "File copying is complete"