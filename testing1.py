import sys
a = sys.argv[1]
print a
x = "ACGTGCGTTAC"
AinX = x.count("A")
CinX = x.count("C")
GinX = x.count("G")
TinX = x.count("T")
print AinX
print CinX
print GinX
print TinX

#T = 2 * (# of A or T nucleotides) + 4 * (# of G or C nucleotides)
y = "ACGTGCCCCCTAGC"
AnTinY = y.count("A") + y.count("T")
GnCinY = y.count("G") + y.count("C")
T = 2 * (AnTinY) + 4 * (GnCinY)
print T