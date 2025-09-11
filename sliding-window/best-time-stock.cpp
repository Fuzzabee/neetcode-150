// You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
// 
// You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
// 
// Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
// 
// Input: prices = [10,1,5,6,7,1]
// Output: 6
// 
// Input: prices = [10,8,7,5,2]
// Output: 0

#include <iostream>
#include <vector>

int maxProfit(std::vector<int>& prices) {
    int lowestValue = prices.front();
    int highestValue = prices.front();
    int largestProfit = 0;

    for (int i = 0; i < prices.size(); i++) {
        if (prices.at(i) < lowestValue) {
            lowestValue = prices.at(i);
            highestValue = prices.at(i);
        } else if (prices.at(i) > highestValue) {
            highestValue = prices.at(i);
        }

        if ( (highestValue - lowestValue) > largestProfit) {
            largestProfit = highestValue - lowestValue;
        }
    }

    return largestProfit;
}

void runTestSuite() {
    std::vector test1Input = {10, 1, 5, 6, 7, 1};
    int test1Result = maxProfit(test1Input);
    std::cout << "Expected: 6 Actual: " << test1Result << "\n";

    std::vector test2Input = {10, 8, 7, 5, 2};
    int test2Result = maxProfit(test2Input);
    std::cout << "Expected: 0 Actual: " << test2Result << "\n";    
}

int main() {
    runTestSuite();
    return 0;
}