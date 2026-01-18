from typing import List
nums = [1,2,3]
i = 0
n = len(nums) - 1
jump_count = 0
farthest = nums[i]
current_end = 0
while i < len(nums)-1: # iteration until meeting the requirement.
    
    farthest = max(farthest, i + nums[i])
    if len(nums) == 1: # exception 
        i = len(nums)
        break

    if  i == current_end:
        jump_count += 1
        current_end = farthest

    if current_end >= n:
        i = len(nums)
        break
    i += 1
print(jump_count)
