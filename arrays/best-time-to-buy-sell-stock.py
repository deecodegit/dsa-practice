##m1:
def best_time_to_buy_sell_stock(prices):
    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            max_profit = max(max_profit, prices[i] - min_price)
        
    return max_profit

print(best_time_to_buy_sell_stock([7,1,5,3,6,4]))
print(best_time_to_buy_sell_stock([1,2,3,4,5]))
print(best_time_to_buy_sell_stock([7,6,4,3,1]))

##m2:
def best_time_to_buy_sell_stock_optimised(prices):
    min_price = float('inf')
    max_profit = 0

    for i in prices:
        if i < min_price:
            min_price = i
        else:
            max_profit = max(max_profit, i - min_price)
        
    return max_profit

print(best_time_to_buy_sell_stock_optimised([7,1,5,3,6,4]))
print(best_time_to_buy_sell_stock_optimised([1,2,3,4,5]))
print(best_time_to_buy_sell_stock_optimised([7,6,4,3,1]))