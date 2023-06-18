nums = [4,5,6,7,0,1,2]
# print(nums[-1])

def search_element(nums, target, start, end):
    while(start<=end):
        mid = int(start + (end-start)/2)
        print("mid", mid)
        if nums[mid]==target:
            return mid
        elif (mid-1)>=0 and nums[start]<=target<=nums[mid-1]:
            print("case 1")
            end = mid-1
            search_element(nums, target, start, end)
        elif nums[start]<=target:
            print("case 1")
            end = mid-1
            search_element(nums, target, start, end)
        else:
            print("case 2")
            start = mid+1
            search_element(nums, target, start, end)
    return -1
# print(search_element([1,3], 3, 0, 1))

def search_element(nums, target):
    start = 0
    end = len(nums)-1
    while(start<=end):
        mid = int(start + (end-start)/2)
        print("mid", mid)
        if nums[mid]==target:
            return mid
        elif nums[start]<=target or target<nums[mid]:
            print("case 1")
            end = mid-1
            # search_element(nums, target, start, end)
        else:
            print("case 2")
            start = mid+1
            # search_element(nums, target, start, end)
    return -1

# print(search_element([5,1,3], 5))  


def searcH_in_rs_array(nums, target):
    start = 0
    end = len(nums)-1
    while(start<=end):
        mid = int(start + (end-start)/2)
        # print("mid", mid)
        if nums[mid]==target:
            return mid
        elif nums[start]<=nums[mid]:
            # print("case 1")
            if mid-1>=0 and nums[start]<=target<=nums[mid-1]:
                # print("case 2")
                end = mid-1
            else:
                # print("case 3")
                start = mid+1
        elif nums[end]>=nums[mid]:
            # print("case 4")
            if mid+1<len(nums) and nums[mid+1]<=target<=nums[end]:
                # print("case 5")
                start = mid+1
            else:
                # print("case 6")
                end = mid-1
        # print(start)
        # print(end)
    return -1

# nums = [6,7,1,2,3,4,5]
nums = [1,3]
# target = 6
target = 3
print(searcH_in_rs_array(nums, target))
    
    