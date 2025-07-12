### INSTRUCTIONS ###
# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
#
# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
#
# Your solution must run in O(logn)O(logn) time.
#
# Input: nums = [-1,0,2,4,6,8], target = 4
# Output: 3
#
# Input: nums = [-1,0,2,4,6,8], target = 3
# Output: -1
####################

def search(nums, target):
    leftIndex = 0
    rightIndex = len(nums) - 1

    while leftIndex < rightIndex and (rightIndex - leftIndex) > 1:
        nextIndex = (leftIndex + rightIndex) // 2
        print(f"lI:{leftIndex} rI:{rightIndex} nI: {nextIndex}")
        if nums[nextIndex] == target:
            return nextIndex
        elif nums[nextIndex] > target:
            rightIndex = nextIndex
        else:
            leftIndex = nextIndex

    if nums[leftIndex] == target: return leftIndex
    if nums[rightIndex] == target: return rightIndex
    return -1

def main():
    print(search([-1,0,2,4,6,8], 4))
    print(search([-1,0,2,4,6,8], 3))

if __name__ == "__main__":
    main()