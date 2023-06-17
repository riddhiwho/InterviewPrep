s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
        start=0
        end = len(s)-1

        while start<end:
            if not s[start].isalnum():
                start+=1
            elif not s[end].isalnum():
                end-=1
            elif s[start].lower() != s[end].lower():
                return False
            else:
                start+=1
                end-=1
        return True

def isPalindrome1(s):
        s=s.lower()
        new_s=""
        for i in s:
            if 'a'<=i<='z' or '0'<=i<='9':
                new_s+=i
        for i in range(len(new_s)):
            if i>=len(new_s)-i-1 and new_s[i]!=new_s[len(new_s)-i-1]:
                return False
        return True
        
print(isPalindrome1(s))
    