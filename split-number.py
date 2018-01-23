import sys
firstinteger = float(sys.argv[1])
print "%d"%firstinteger
listsplit = sys.argv[1].split(".")
listsplit[0:1] = "0"
string1 = ".".join(listsplit)
print string1