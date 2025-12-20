prices = [7,1,5,3,6,4]
max = 0
min = 0
x = 0
for i in range(len(prices)):
    j = i + 1 
    for j in range(len(prices)):
        if prices[i] <= prices[j]:
            min = prices[i]
            if prices[i] >= prices(j)
            j += 1

        else: 
            min = prices[j]
            i += 1
            
while x < len(prices):
    y = x + 1
    while y < len(prices):    
        if prices[x] >= prices[y]:
            y += 1
            max = prices[x]
        else:
            max = prices[y]
            x += 1
