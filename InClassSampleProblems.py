#import sys
##### From what once was Testing1.py #######
# a = sys.argv[1]
# print a
# x = "ACGTGCGTTAC"
# AinX = x.count("A")
# CinX = x.count("C")
# GinX = x.count("G")
# TinX = x.count("T")
# print AinX
# print CinX
# print GinX
# print TinX
#
# #T = 2 * (# of A or T nucleotides) + 4 * (# of G or C nucleotides)
# y = "ACGTGCCCCCTAGC"
# AnTinY = y.count("A") + y.count("T")
# GnCinY = y.count("G") + y.count("C")
# T = 2 * (AnTinY) + 4 * (GnCinY)
# print T
####################################
#total = 0
#for num in sys.argv[1:]:
#    integernum = int(num)
#    total = total + integernum
#    print total

#maxnum = int(sys.argv[1])
#total = 0
#square = 0
#while ( total < maxnum):
#    square = square + 1
#    total = square * square
#    print total

def fibonacci(n, start1 = 0, start2 = 1):
    list = [start1, start2]
    for i in range(2, n):
        list.append(list[i-1] + list[i-2])
    ratio = float(list[n-1])/float(list[n-2])
    return [list[0:n], ratio]

print fibonacci(10, 4, 7)