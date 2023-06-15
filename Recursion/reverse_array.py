list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def rev_list_rec(list, i):
    if i==0:
        return
    else:
        print(list[i-1], end= " ")
        rev_list_rec(list, i-1)
        
# rev_list_rec(list1, len(list1))

def swap_elements(list1, i1, i2):
    list1[i1], list1[i2] = list1[i2], list1[i1]
    return list1

# print(swap_elements(list1, 0, 1))

def rev_list_rec1(list, i1, i2):
    if i1>=i2:
        return list
    else:
        l = swap_elements(list, i1, i2)
        # print(l)
        return rev_list_rec1(l, i1+1, i2-1)

# l = rev_list_rec1(list1, 0, len(list1)-1)
# for i in l:
#     print(i, end= " ") 
    
def rev_list_rec2(list, i):
    if i>=len(list)//2:
        return list
    else:
        l = swap_elements(list, i, len(list)-i-1)
        return rev_list_rec2(l, i+1)

new_list = rev_list_rec2(list1, 0)
for i in new_list:
    print(i, end= " ")
  

# list1 = rev_list_rec1(list1, 0, len(list1)-1)
# for i in list1:
#     print(i, end= " ")


# def rev_list_rec1(list, i):
    
        

def rev_list0(list):
    for i in range(len(list)):
        # print(list1[i], end= " ")
        print(list[len(list)-i-1], end= " ")
    
# rev_list0(list1)

def rev_list1(list):
    revd_list = list[::-1]
    for i in revd_list:
        print(i, end= " ")
        
# rev_list1(list1)

def rev_list2(list):
    for i in range(len(list)-1,-1,-1):
        print(list[i], end= " ")

# rev_list2(list1)