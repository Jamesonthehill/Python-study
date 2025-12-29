

# 122. Best Time to Buy and Sell Stock II
prices = [7,1,5,3,6,4]
i = 0
current_profit = 0
total_profit = 0

while i < len(prices):
    j = i + 1
    while j < len(prices):
        if prices[i] > prices[j]:
            break
        else:
            current_profit = prices[j] - prices[i]
            total_profit += current_profit 
    i += 1