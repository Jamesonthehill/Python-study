
nums = [3,2,1,0,4]
judge = True
max_reach = 0
last_index = len(nums) - 1

for i in range(len(nums)):
    # If we are at an index that is unreachable, we fail
    if i > max_reach:
        judge = False
        break
    # Update the farthest we can reach from here
    max_reach = max(max_reach, i + nums[i])
    
    # If we can already reach the end, we win
    if max_reach >= last_index:
        judge = True
                
print(judge)