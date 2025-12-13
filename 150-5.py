
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for x in nums:
            if count == 0:
                candidate = x
            
            if x == candidate:
                count += 1
            else:
                count -= 1

        return candidate

print(candidate := Solution().majorityElement([2,2,1,1,1,2,2,1,1,3,3,3])) 
# nums = [1]
# i = 0 
# final = 0
# count = 0
# k = 0 
# while i < len(nums):
#     j = i + 1
#     while j < len(nums):
#         if nums[i] == nums[j]:
#             count += 1
#         j+=1
#     if count > final:
#         final = count
#         k = nums[i]
#     count = 0
#     i += 1

#     print ("k =", k)
