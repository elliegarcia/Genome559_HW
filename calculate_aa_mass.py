import sys
massesfile = open(sys.argv[2],"r")
aminoacidfile = open(sys.argv[3], "r")

massesdictionary = {}
for amino in massesfile:
    line = amino.strip().split(",")
    massscore = float(line[1])
    masskey = line[0]
    massesdictionary[masskey] = massscore

answer = massesdictionary['A'] + massesdictionary['T']
print answer