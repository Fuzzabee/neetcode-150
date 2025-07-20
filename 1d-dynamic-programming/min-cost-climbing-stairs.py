### INSTRUCTIONS ###
# You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase.
# After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.
#
# You may choose to start at the index 0 or the index 1 floor.
#
# Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.
#
# Input: cost = [1,2,3]
# Output: 2
#
# Input: cost = [1,2,1,2,1,1,1]
# Output: 4
####################

def minCostClimbingStairs(cost):
    if not cost: return -1
    if len(cost) == 1: return cost[0]
    if len(cost) == 2: return min(cost[0], cost[1])

    totalCost = [cost[-1], cost[-2]]
    for i in range(len(cost) - 3, -1, -1):
        curStairCost = cost[i]
        bestCost = min(totalCost[-1], totalCost[-2])
        totalCost.append(curStairCost + bestCost)

    return min(totalCost[-1], totalCost[-2])

def main():
    print(minCostClimbingStairs([1,2,3]))
    print(minCostClimbingStairs([1,2,1,2,1,1,1]))

if __name__ == "__main__":
    main()