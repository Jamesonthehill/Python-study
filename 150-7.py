prices = [2,4,1]

# i = 0
# max = 0
# min = prices[i]
# for i in len(prices):
#     if prices[i]
x = 0
i = 0
total = 0
max = prices[x]
min = prices[i]
while i < len(prices):
    if prices[i] < min:
        min = prices[i]
        total = max - min
        x = i
        if i == len(prices)-1:
                break
    i += 1

    if prices[x] > max: 
        max = prices[x]
        if x == len(prices)-1:
            break
    x += 1
print(total)

# while x < len(prices):
#     if prices[x] > max: 
#         max = prices[x]
#         if x == len(prices)-1:
#             break
#     x += 1