#GIVEN: a file with multiple lines RETURN: the lines of the file in reverse order
import sys
ogfile = open(sys.argv[1], "r") #the file used must have a carriage return at the end of the last line
ogstring = ogfile.readlines()
oglist = list(ogstring)
oglist.reverse()
newstring = "".join(oglist)
ogfile.close()
print newstring