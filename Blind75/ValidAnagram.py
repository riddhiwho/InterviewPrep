def isAnagram(s1, s2):
        dict = {}
        for i in s1:
            if i in dict.keys():
                dict[i]+=1
            else:
                dict[i]=1
                
        for j in s2:
            if j in dict and dict[j]>0:
                dict[j]-=1
            else:
                return False
        
        for key, _ in dict.items():
            if dict[key]>0:
                return False
            
        return True
    
print(isAnagram("anagram", "nagaram"))