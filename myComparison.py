
## This function sorts in a case-insensitive alphabetical order, but with caps preceding in case of a tie
def myComparison(a, b): # honestly I don't fully understand what I did
    c = a.lower()
    d = b.lower()
    if c < d:
        return -1
    elif c > d:
        return 1
    elif a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

### Running the function ####
mylist = ['Jim', 'jim', 'jiM', 'Jimmy', 'elhanon', 'Elhanon']
mylist.sort(myComparison)
print mylist