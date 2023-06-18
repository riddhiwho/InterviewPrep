def check_pal(str, i):
    if i>=len(str)//2:
        return True
    else:
        if str[i]!=str[len(str)-i-1]:
            return False
        else:
            return check_pal(str, i+1)
        
print(check_pal("abbac", 0))