        
nums =[2,2,1,1,1,2,2]
candidate = None
count = 0
i = 0
for x in nums:
    if count == 0:
        candidate = x
    if nums[i] == candidate:
        count += 1
    if nums[i] != candidate:
        count -= 1
    i += 1

    