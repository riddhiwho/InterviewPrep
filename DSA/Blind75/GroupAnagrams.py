strs = ["eat","tea","tan","ate","nat","bat"]
def group_anagrams(s):
    
    dict = {}
    final_list = []
    
    for i in strs:
        sorted_word = ''.join(sorted(i))
        if sorted_word in dict.keys():
            dict[sorted_word].append(i)
        else:
            dict[sorted_word]=[i]
    
    for _, value in dict.items():
        final_list.append(value)
    
    return final_list

print(group_anagrams(strs))