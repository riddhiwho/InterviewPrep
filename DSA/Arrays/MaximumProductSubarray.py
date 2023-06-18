'''
case1: when all the elements are +ve
case2: when we have even -ve elements
case3: when we have odd -ve elements
case4: when we have 0
'''

# list = [3,2,-1,4,-6,3,-2,6]
# list = [2,3,-2,4]
# list = list[1:3]
# print(list)
list = [-2,3,4,-1,0,-2,3,1,4,0,4,6,-1,4]

def maxProduct(nums):
        pre = 1
        suff = 1
        ans = float('-inf')

        for i in range(len(nums)):
            if pre==0:
                pre=1
            if suff==0:
                suff=1
            
            pre = pre*nums[i]
            suff = suff*nums[len(nums)-i-1]
            ans = max(ans, max(pre, suff))
        return ans
