nums = [-1,1,0,-3,3]

pre = [1]*len(nums)
post = [1]*len(nums)

for i in range(1, len(nums)):
    pre[i] = nums[i-1]*pre[i-1]
    post[len(nums)-i-1] = nums[len(nums)-i]*post[len(nums)-i] 
for i in range(len(nums)):
    nums[i] = pre[i]*post[i]
print(nums)