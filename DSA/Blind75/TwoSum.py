list = [2,7,7,11,-2,15]
target = 9

#exactly 1 pair
def two_sum_pair(list, target):
    dict = {}
    for i in list:
        if (target-i) in dict.keys():
            return list.index(i), list.index(target-i)
        else:
            dict[i]=list.index(i)

#0 or more pairs
def all_two_sum_pairs(list, target):
    dict = {}
    final_list = []
    for i in range(len(list)):
        if (target-list[i]) in dict.keys():
            # actual elements
            # final_list.extend([(list[i], target-list[i])])
            # index of elements
            final_list.extend([(i, dict[target-list[i]])])
        else:
            dict[list[i]]=i
    return final_list

list_of_indices = all_two_sum_pairs(list, target)
print(list_of_indices)