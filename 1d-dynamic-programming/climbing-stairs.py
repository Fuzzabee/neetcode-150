### INSTRUCTIONS ###
# You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.
#
# Return the number of distinct ways to climb to the top of the staircase.
#
# Input: n = 2
# Output: 2
#
# Input: n = 3
# Output: 3
####################


def climbStairs(n):
    results = []
    for i in range(n):
        if i == 0: results.append(1)
        elif i == 1: results.append(2)
        else:
            results.append(results[i - 1] + results[i - 2])

    return results[-1]

def main():
    print(climbStairs(2))
    print(climbStairs(3))
    print(climbStairs(4))
    print(climbStairs(15))
    print(climbStairs(30))

if __name__ == "__main__":
    main()