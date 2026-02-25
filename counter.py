#data structure - Dictionary
#it is a collection of  {key1 : value1, key2 : value2}
#insertions and deletions or updations are super fast here

s = "the sun rises in the east and Messi is the best player in the world"
def counter(s):
    d = {}
    #split function will break a sentence into words
    #seperator will do the breaking - default is space
    words = s.split()
    # print(words) #we have the list of words
    for word in words:
        #check if this word is already in the dictionary
        if word.lower() in d:
            d[word.lower()] += 1
        else:
            d[word.lower()] = 1
    print(d)



# print("Hey enter a sentence:") #this will prompt us to enter a sentence
# s = input() #this will take the input
counter(s)