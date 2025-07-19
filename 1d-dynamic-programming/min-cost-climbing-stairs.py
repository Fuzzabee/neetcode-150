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
    return -1

def main():
    print(minCostClimbingStairs([1,2,3]))
    print(minCostClimbingStairs([1,2,1,2,1,1,1]))

if __name__ == "__main__":
    main()