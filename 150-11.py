# Hindex     
import math
citations = [3,0,6,1,5]
total = 0
tempo = 0
final = 0
for i in range(len(citations), 0):
    
    # H-index cannot be bigger than len[citations]


    if i == len(citations)-1:
        final = total / len(citations)
        final = math.trunc(final)

print(final)