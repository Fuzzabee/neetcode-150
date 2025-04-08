# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

def maxProfit(prices):
    if len(prices) == 0: return 0
    
    # Initial variable setup
    buy = prices[0]
    sell = prices[0]
    profit = sell - buy

    # Loop through each value, checking for a new low buy point, and comparing all sell points to the lowest available buy, updating when necessary
    for n in prices:
        if n < buy:
            buy = n
            sell = n
            continue
        if n > sell:
            sell = n
            if sell - buy > profit:
                profit = sell - buy
    
    return profit

def main():
    # Input: prices = [10,1,5,6,7,1]
    # Output: 6
    prices = [10,1,5,6,7,1]
    print(maxProfit(prices))

    # Input: prices = [10,8,7,5,2]
    # Output: 0
    prices = [10,8,7,5,2]
    print(maxProfit(prices))

if __name__ == "__main__":
    main()