#import sys
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

def fibonacci(n):
    list = [0, 1]
    for i in range(2, n):
        list.append(list[i-1] + list[i-2])
    return list[0:n]
print fibonacci(10)