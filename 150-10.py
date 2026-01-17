from typing import List
i = 0
nums = [1,2,1,1,1]
n = len(nums) - 1
jump_count = 0
farthest = nums[0]
while i < len(nums):
    
    farthest = max(farthest, nums[i])

    if len(nums) == 1 or nums[i] == 0:
        i = n
        break
    
    if farthest >= n:
        i = len(nums)
        break

    jump_count += farthest
    i += 1 

print(i)
