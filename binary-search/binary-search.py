# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
# Your solution must run in O(logn) time.

def search(nums, target):
    leftIndex = 0
    rightIndex = len(nums) - 1
    while leftIndex < rightIndex:
        newIndex = ( leftIndex + rightIndex ) // 2
        if nums[newIndex] == target: 
            return newIndex
        elif nums[newIndex] < target: 
            leftIndex = newIndex + 1
        else:
            rightIndex = newIndex - 1
    
    if nums[leftIndex] == target: return leftIndex
    return -1

def main():
    # Input: nums = [-1,0,2,4,6,8], target = 4
    # Output: 3
    nums = [-1,0,2,4,6,8]
    target = 4
    print(search(nums, target))

    # Input: nums = [-1,0,2,4,6,8], target = 3
    # Output: -1
    target = 3
    print(search(nums, target))

if __name__ == "__main__":
    main()