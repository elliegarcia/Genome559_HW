import sys
#total = 0
#for num in sys.argv[1:]:
#    integernum = int(num)
#    total = total + integernum
#    print total

hellofile = open("Hello.txt", "r")

for line in hellofile:
    for word in line.split():
        print len(word)
hellofile.close()