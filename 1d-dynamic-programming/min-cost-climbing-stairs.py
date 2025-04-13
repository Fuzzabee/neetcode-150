# You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.
# You may choose to start at the index 0 or the index 1 floor.
# Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.
    # 2 <= cost.length <= 100
    # 0 <= cost[i] <= 100


def minCostClimbingStairs(cost):
    totalCosts = [0] * len(cost)
    totalCosts[0] = cost[0]
    totalCosts[1] = cost[1]

    for i in range(2, len(totalCosts)):
        totalCosts[i] = cost[i] + min(totalCosts[i - 1], totalCosts[i - 2])

    return min(totalCosts[-1], totalCosts[-2])

def main():
    # Input: cost = [1,2,3]
    # Output: 2
    print(minCostClimbingStairs([1,2,3]))

    # Input: cost = [1,2,1,2,1,1,1]
    # Output: 4
    print(minCostClimbingStairs([1,2,1,2,1,1,1]))

if __name__ == "__main__":
    main()