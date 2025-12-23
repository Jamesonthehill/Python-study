#121. Best Time to Buy and Sell Stock
prices = [7,1,5,3,6,4]
i = 0
min = prices[0]
max = 0
while i < len(prices):
    price = prices[i]
   
    if price < min:
        min = price

    else:
        profit = price - min
        if profit > max: 
            max = profit
    i += 1
print(max)
# while x < len(prices):
#     if prices[x] > max: 
#         max = prices[x]
#         if x == len(prices)-1:
#             break
#     x += 1
