# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

def main():
    # Input: nums = [1, 2, 3, 3]
    # Output: true
    nums = [1,2,3,3]
    print(hasDuplicate(nums))

    # Input: nums = [1, 2, 3, 4]
    # Output: false
    nums = [1,2,3,4]
    print(hasDuplicate(nums))

def hasDuplicate(nums) -> bool:
    frequency = dict()
    for n in nums:
        if n in frequency:
            return True
        else:
            frequency[n] = 1

    return False

if __name__ == "__main__":
    main()