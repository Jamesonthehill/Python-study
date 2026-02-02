# Hindex     
citations = [3,0,6,1,5]
total = []

citations.sort(reverse=True)
Ascend = citations
print(Ascend)
print(citations)
count = 0
i = 0
final = 0
while i < len(citations):
    if Ascend[i] >= i+1:
        final = Ascend[i]
    i += 1

print(final)