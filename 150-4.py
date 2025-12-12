
# nums = [0,0,1,1,1,1,2,3,3]

# i = 0 
# while i < len(nums):
#     j = i + 1
#     while j < len(nums):
#         if nums[i] == nums[j]:
#             if nums[i] == nums[i-1] and j > 1:
#                 del nums[j]
#             else:
#                 j += 1
#         else:
#             j += 1
#     i += 1

# print(nums)

# print(nums[:i]) --- IGNORE ---
nums = [0,0,1,1,1,1,2,3,3]
i = 0  # i = slow, j = fast (reader)
for num in nums: # unique way of python3
    if i < 2 or num != nums[i-2]:
        nums[i] = num
        i += 1
# return i
