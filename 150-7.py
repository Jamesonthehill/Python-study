prices = [7,1,5,3,6,4]
max = 0
min = 0
x = 0
i = 0
while i < len(prices):
    if i < 1 or prices[i] < min:
        min = prices[i]
        x = i
        if i == len(prices)-1:
                break
    i += 1

while x < len(prices):
    if prices[x] > max: 
        max = prices[x]
        if x == len(prices)-1:
            break
    x += 1

print(max-min)