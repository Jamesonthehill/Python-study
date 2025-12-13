        
# 150-6 Rotate Array
nums = [1,2,3,4,5,6,7]
i = 0 
for x in nums:
    nums.insert((i + 3) % len(nums), x)
    i += 1
    del nums[i]