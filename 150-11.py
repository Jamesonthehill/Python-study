# Hindex     
import math
citations = [3,0,6,1,5]
i = 0 
total = 0
number = 0
for i in range(0, len(citations)):
    total += citations[i]

    if i == len(citations)-1:
        number = total / len(citations)
        number = math.trunc(number)

print(number)