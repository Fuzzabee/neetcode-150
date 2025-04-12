import bisect

# You are given an array of integers stones where stones[i] represents the weight of the ith stone.
# We want to run a simulation on the stones as follows:
#     At each step we choose the two heaviest stones, with weight x and y and smash them togethers
#     If x == y, both stones are destroyed
#     If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# Continue the simulation until there is no more than one stone remaining.
# Return the weight of the last remaining stone or return 0 if none remain.

def lastStoneWeight(stones):
    if not stones: return 0
    stones.sort()

    while len(stones) > 1:
        x = stones.pop()
        y = stones.pop()
        if x != y:
            bisect.insort(stones, abs(x - y))
    
    return 0 if not stones else stones.pop()

def main():
    # Input: stones = [2,3,6,2,4]
    # Output: 1
    print(lastStoneWeight([2,3,6,2,4]))

    # Input: stones = [1,2]
    # Output: 1
    print(lastStoneWeight([1,2]))

    # Input: stones = [2,2]
    # Output: 0
    print(lastStoneWeight([2,2]))

    # Input: stones = [7,6,7,6,9]
    # Output: 3
    print(lastStoneWeight([7,6,7,6,9]))

if __name__ == "__main__":
    main()