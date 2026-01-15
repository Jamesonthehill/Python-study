from typing import List
i = 0
nums = [1,2,1,1,1]
n = len(nums) - 1
jump_count = 0


class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        n = len(nums) - 1
        jump_count = 0
        # while i < n-i:
        for i in range(0, len(nums)-1):
            
            if len(nums) == 1 or nums[i] == 0:
                i = n
                break
            
            if nums[i] + i >= n:
                jump_count += 1
                i = len(nums)
                break
        
            else:
                jump_count += 1
        
        return jump_count
    
print(jump_count)