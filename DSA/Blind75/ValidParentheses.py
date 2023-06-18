def isValid(s):
        brackets_dict = {"(":")", "[":"]", "{":"}"}
        list = []
        for i in s:
            if i in brackets_dict:
                list.append(i)
            elif len(list)==0 or i!=brackets_dict[list.pop()]:
                return False
        return len(list)==0

print(isValid("(]"))
        