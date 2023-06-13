nums = [1,1,1,3,3,4,3,2,4,2, 5]

# sort and compare
def duplicate_elements(list):
    list.sort()
    final_set = set()
    for i in range(len(list)-1):
        if list[i]==list[i+1]:
            final_set.add(list[i])

    return final_set

# dupl_ele = duplicate_elements(nums)
# print(dupl_ele)


# dictionary
def duplicate_elements_1(list):
    dict = {}
    final_set =set()
    for i in list:
        if i in dict.keys():
            final_set.add(i)
        else:
            dict[i]=list.index(i)
    return final_set

dupl_ele = duplicate_elements_1(nums)
print(dupl_ele)