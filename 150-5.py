   
nums = [2,2,1,1,1,2,2]
i = 0 
final = 0
count = 0

while i < len(nums):
    if count > final:
        final = count
        nums[i] = nums[j]
    j = i + 1
    count = 0
    while j < len(nums):
        if nums[i] == nums[j]:
            count += 1
        j+=1
    i += 1