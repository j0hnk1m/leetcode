prices = [7,1,5,3,6,4]

if not prices:
    return 0

lowest_price = prices[0]
max_profit = 0
for i in prices[1:]:
    lowest_price = min(lowest_price, i)
    max_profit = max(max_profit, i-lowest_price)

return max_profit
