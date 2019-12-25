prices = [7,1,5,3,6,4]

lowest_price = float('inf')
profit = 0
for p in prices:
    if p < lowest_price:
        lowest_price = p
    elif p - lowest_price > profit:
        profit = p - lowest_price

return profit
