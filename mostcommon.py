import sys
#myDict = {"Curly":4123, "Larry":2057, "Moe":1122}
#print myDict.keys()[myDict.values().index(1122)]
speechfile = open(sys.argv[1], "r")

def prepare_file_for_dict(myfile):
    mystring = myfile.read()
    mystring = mystring.replace('\r', '')
    mystring = mystring.replace('\n', '')
    mystring = mystring.replace('.', '')
    mystring = mystring.replace(',', '')
    mystring = mystring.replace("'", '')
    mystring = mystring.replace('"', '')
    mystring = mystring.replace('?', '')
    mystring = mystring.replace('#', '')
    mystring = mystring.replace(';', '')
    mystring = mystring.replace(':', '')
    mystring = mystring.replace('-', '')
    mystring = mystring.replace('(', '')
    mystring = mystring.replace(')', '')
    mystring = mystring.replace('!', '')
    mystring = mystring.lower()
    mystring = mystring.strip()
    mylist = mystring.split(' ')
    return mylist

text = prepare_file_for_dict(speechfile)

querylength = int(sys.argv[2])
word_dict = {}
counts = 0

for item in text:
    itemlength = len(item)
    if itemlength > querylength:
        if (item in word_dict):
            word_dict[item] += 1
        else:
            word_dict[item] = int(1)