        
# 150-6 Rotate Array
nums = [1,2,3,4,5,6,7]
i = 0 
print(nums[::2])    # every 2nd element
print(nums[::-1])   # reversed copy of the list

nums[:] = nums[-3:] + nums[:-3]
print(nums[:])
 
 
