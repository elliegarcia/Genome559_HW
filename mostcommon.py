import sys
## This function reads the file and strips it of any carriage returns and punctuation
def prepare_file_for_dict(myfile): # the argument is an opened file
    mystring = myfile.read() # reads the file into a string
    mystring = mystring.replace('\r', '') # gets rid of carriage returns
    mystring = mystring.replace('\n', '')
    mystring = mystring.replace('.', '') # strips file of punctuation from here on down
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
    mystring = mystring.lower() # makes everything lowercase
    mystring = mystring.strip() # strips \n and \r from the beginning and end
    mylist = mystring.split(' ') # splits the file into a list of words
    return mylist # returns the list of words

## This function puts the words from the text into a dictionary with the counts as values
def make_word_dict(mytext, querylength):
    querylength = int(querylength)
    word_dict = {} # initialize the dictionary
    for item in mytext: # put new words into a dictionary with the word counter
        itemlength = len(item) # give the length of the word
        if itemlength >= querylength: # if the length of the word >= the query
            if (item in word_dict): # search for the word in the dictionary
                word_dict[item] += 1 # if it's there add +1 to the counter
            else:
                word_dict[item] = int(1) # if it's not there add it to the dictionary
        else:
            continue # if the length of the word < the query than keep going
    return word_dict

## This function finds the most common word(s) from the dictionary
def most_common_word(dictionary):
    numvalues = len(dictionary.values())
    values_sorted = sorted(dictionary.values())
    highest_count = values_sorted.pop(numvalues - int(1))
    return [word for word, count in dictionary.items() if count == highest_count]

## This function finds the number of times the most common word(s) occurs
def countof_most_common_word(dictionary):
    numvalues = len(dictionary.values())
    values_sorted = sorted(dictionary.values())
    highest_count = values_sorted.pop(numvalues - int(1))
    return highest_count
##################### Running the functions ###########################
anyfile = open(sys.argv[1], "r") # open the file
anytext = prepare_file_for_dict(anyfile) # prepare the file
word_dictionary = make_word_dict(anytext, sys.argv[2]) # make the dictionary
most_common = most_common_word(word_dictionary) # find the most common word(s)
countmostcommon = countof_most_common_word(word_dictionary) # find the counts corresponding with those word(s)

for word in most_common:
    print word, countmostcommon # display words & counts the way Lindsay wants

anyfile.close()