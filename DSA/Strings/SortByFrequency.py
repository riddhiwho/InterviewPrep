#sort by frequency, and lexicographically for the ones with same frequency
#return the most frequent string(s)


import operator

arr = [ "geeks", "for", "geeks", "a", "portal", "to", "learn", "can", "be", "computer", "science", "zoom", "yup", "fire", "in", "be", "data", "geeks",]

def sortByFreq(arr):
    word_count = {}
    for i in arr:
        if i in word_count.keys():
            word_count[i]+=1
        else:
            word_count[i]=1
            
    sorted_d = dict( sorted(word_count.items(), key=operator.itemgetter(1),reverse=True))
    
    for key, value in sorted_d.items():
        print(key)
        
sortByFreq(arr)
    
    
