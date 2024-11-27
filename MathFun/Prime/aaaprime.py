p = 0
s = 2
nums = []

while s <= 7:
    nums.append(s)
    s = s+1

while len(nums) > p:
    k = nums[p]
    for i in nums:
        if not i == k and i%k == 0:
            nums.remove(i)
    p = p+1
    
    
print(nums)
