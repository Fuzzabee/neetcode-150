# You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.
# Return the number of distinct ways to climb to the top of the staircase. 

# Attempt 04/09/25
# def climbStairs(n):
#     uniqueWays = 0
#     uniqueWays += climb(1, n)
#     uniqueWays += climb(2, n)
#     return uniqueWays

# def climb(currentN, n):
#     if n == currentN:
#         return 1

#     if n < currentN:
#         return 0

#     uniqueWays = 0
#     uniqueWays += climb(currentN + 1, n)
#     uniqueWays += climb(currentN + 2, n)
#     return uniqueWays

def climbStairs(n):
    if n == 1: return 1

    curIndex = n
    stairsClimbed = [0] * ( n + 1 )
    stairsClimbed[curIndex] = 1
    curIndex -= 1
    stairsClimbed[curIndex] = 1
    curIndex -= 1

    while curIndex >= 0:
        stairsClimbed[curIndex] = stairsClimbed[curIndex + 1] + stairsClimbed[curIndex + 2]
        curIndex -= 1

    print(stairsClimbed)
    return stairsClimbed[0]

def main():
    # Input: n = 2
    # Output: 2
    print(climbStairs(2))

    # Input: n = 3
    # Output: 3
    print(climbStairs(3))

    print(climbStairs(100))

if __name__ == "__main__":
    main()