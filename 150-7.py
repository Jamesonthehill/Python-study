prices = [1]

# i = 0
# max = 0
# min = prices[i]
# for i in len(prices):
#     if prices[i]
x = 0
i = 0
total = 0
max = 0
min = prices[i]
while i < len(prices):
    if i < 1 or prices[i] < min:
        min = prices[i]
    if len(prices) == 1:
        total = 0
        break
    i += 1
    x = i
    if x < 1 or prices[x] > max: 
        max = prices[x]
        total = max - min
        if total <= 0:
            total = 0
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