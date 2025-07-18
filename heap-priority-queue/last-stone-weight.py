### INSTRUCTIONS ###
# You are given an array of integers stones where stones[i] represents the weight of the ith stone.
#
# We want to run a simulation on the stones as follows:
#
#     At each step we choose the two heaviest stones, with weight x and y and smash them togethers
#     If x == y, both stones are destroyed
#     If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
#
# Continue the simulation until there is no more than one stone remaining.
#
# Return the weight of the last remaining stone or return 0 if none remain.
#
# Input: stones = [2,3,6,2,4]
# Output: 1
#
# Input: stones = [1,2]
# Output: 1
####################

def lastStoneWeight(stones):
    curStones = stones.copy()
    curStones.sort()
    while len(curStones) > 1:
        stoneX = curStones.pop()
        stoneY = curStones.pop()
        if stoneX == stoneY: continue
        else:
            newWeight = stoneX - stoneY
            # Using a VERY lazy way of inserting instead of finding correct position in O(logn)
            curStones.append(newWeight)
            curStones.sort()

    return curStones[0]

def main():
    print(lastStoneWeight([2,3,6,2,4]))
    print(lastStoneWeight([1,2]))

if __name__ == "__main__":
    main()