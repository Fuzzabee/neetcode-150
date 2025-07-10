### INSTRUCTIONS ###
# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
#
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
#
# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
#
# Input: prices = [10,1,5,6,7,1]
# Output: 6
#
# Input: prices = [10,8,7,5,2]
# Output: 0
####################

def maxProfit(prices):
    if len(prices) < 2:
        return 0

    lowestBuy = prices[0]
    currentIndex = 0
    currentProfit = 0

    while currentIndex < len(prices):
        if prices[currentIndex] < lowestBuy:
            lowestBuy = prices[currentIndex]
        elif (prices[currentIndex] - lowestBuy) > currentProfit:
            currentProfit = prices[currentIndex] - lowestBuy

        currentIndex += 1

    return currentProfit

def main():
    print(maxProfit([10,1,5,6,7,1]))
    print(maxProfit([10,8,7,5,2]))

if __name__ == '__main__':
    main()