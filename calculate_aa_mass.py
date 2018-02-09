import sys  # IMPORTANT LIMITATION: THE QUERY MUST BE > 1
massesfile = open(sys.argv[2],"r")
massesdictionary = {}
for amino in massesfile:  # put masses file in a dictionary
    line = amino.strip().split(",")
    massvalue = float(line[1])
    masskey = line[0]
    massesdictionary[masskey] = massvalue

nitrogensfile = open(sys.argv[3], "r")
nitrogensdictionary = {}
for nitrogen in nitrogensfile:  # put the nitrogens file in a dictionary
    nline = nitrogen.strip().split(",")
    nitrogenvalue = int(nline[1])
    nitrogenkey = nline[0]
    nitrogensdictionary[nitrogenkey] = nitrogenvalue

query = list(sys.argv[1])
count = 0
monomass = massesdictionary[query[0]]  # made base number for the monoisotopic mass calculation
for pep in range(1,len(query)):  # added the monoisotopic masses in the query together
    count += 1
    monomass = monomass + massesdictionary[query[count]]
monomass = monomass + int(18)  # added the N-terminus weight to the mass

count = 0
nitrocount = nitrogensdictionary[query[0]] # made a base number for the nitrogen calculation
for nitro in range(1,len(query)):  # added the nitrogens in the query together
    count += 1
    nitrocount += nitrogensdictionary[query[count]]
nitrocount = nitrocount * float(0.997)
heavymass = monomass + nitrocount  # calculated the heavymass
print "The peptide ACDEK has a monoisotopic mass of %.3f" %monomass, "and a heavy-N mass of %.3f" %heavymass