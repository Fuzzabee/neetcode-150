### INSTRUCTIONS ###
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
#
# Input: nums = [1, 2, 3, 3]
# Output: true
#
# Input: nums = [1, 2, 3, 4]
# Output: false
####################

def hasDuplicate(nums):
    numsSet = set(nums)
    if len(nums) == len(numsSet):
        return False
    return True

def main():
    print(hasDuplicate([1, 2, 3, 3]))
    print(hasDuplicate([1, 2, 3, 4]))

if __name__ == "__main__":
    main()