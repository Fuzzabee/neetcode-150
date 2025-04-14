# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first. 

def twoSum(nums, target):
    numsNeeded = {}
    for i in range(len(nums)):
        if nums[i] in numsNeeded.keys():
            return [numsNeeded.get(nums[i]), i]
        numsNeeded[(target - nums[i])] = i

def main():
    # nums = [3,4,5,6], target = 7
    # Output: [0,1]
    print(twoSum([3,4,5,6], 7))

    # Input: nums = [4,5,6], target = 10
    # Output: [0,2]
    print(twoSum([4,5,6], 10))

    # Input: nums = [5,5], target = 10
    # Output: [0,1]
    print(twoSum([5,5], 10))


if __name__ == "__main__":
    main()