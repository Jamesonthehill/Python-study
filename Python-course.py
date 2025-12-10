Integer = 11
Alpha = 'Mario'
ss = '11'


# print(Alpha + str(Integer))
# print(10 + int(ss))

# age = 18
# isHappy = False

# if age > 29:
#     print('you are old!')
# elif age >= 18:
#     print('you are getting old!')
# else:
#     print('you are still young!')
    
# if isHappy:
#     print('Happy Thankgiving')
# else: 
#     print('Proud of yourself')

i = 124
# even if we assign the i value, if we use again, it would be overwritten.
for i in range(3):
        print('Hello', i+3)


print (range(3))

# name_list = ['jacob', 'Lee', 'hanse']

# for name in name_list:
#     print(name)

# while True:
#       user_input = input('entersometing >>')
#       if user_input == '0':
#             print('we are done here')
#             break
      

# def say_hello(name):
#       print('Hey there', name)

# say_hello('mario')

# def get_internet():
#       pass

# number = input('Please provide a number >>')

# try:
#     print(10 + int(number))
# except:
#     print('that is not a valid number!')



num1 = [1,2,3]
num2 = [4,5,6]
merge_array = num1 + num2
print(merge_array)


## leetscode pattern 
# i = m - 1
# j = n - 1
# k = m + n - 1

# while j >= 0:
#     if i >= 0 and nums1[i] >= nums2[j]:
#         nums1[k] = nums1[i]
#         i -= 1
#     else:
#         nums1[k] = nums2[j]
#         j -= 1
#     k -= 1

############## Leetscode Remove Element
alpha = [1, 2]
alphaka = len(alpha)
print(alphaka)

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         i = len(nums) - 1

#         while i >= 0:
#             if nums[i] == val:
#                 del nums[i]
#                 i -= 1
#             else:
#                 nums[i] == nums[i]
#                 i -= 1
# Second way using For clause.
# i = len(nums)
# j = len(nums) - 1

# for a in range(i):
#     if nums[j] != val:
#         i -= 1
#         j -= 1
#     else:
#         del nums[j]
#         i -= 1
#         j -= 1

# thrid way using For clause with different approach.
#        i = 0 

#         while i < len(nums):
#             if nums[i] == val:
#                 del nums[i]
#             else:
#                 i += 1

# J = 10 

# for o in range(J):
#     print(o)


# jacob = [10, 20, 30]

# for x in range(len(jacob)):
#     print(jacob[x])

nums = [0, 0, 1, 1, 2, 2, 3, 3, 3, 4]

# print("==============")
# for i in range(len(num33)):
#     j = i + 1
#     for j in range(len(num33)):
#         print(i, j)


print("========duplicate removal======")

def duplicateRemove(nums):
    i = 0 
    for j in range(1,len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

example = [1,1,2,2,2,2,3,3,3,3,4,4,5,6,7]
k = duplicateRemove(example)
print(k)
print(nums[:k])
print(nums[:i])



assert example == [1,1,2,2,2,2,3,3,3,3,4,4,5,6,7]
raise AssertionError("Mismatch")
