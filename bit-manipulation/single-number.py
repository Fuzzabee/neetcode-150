### INSTRUCTIONS ###
# You are given a non-empty array of integers nums. Every integer appears twice except for one.
#
# Return the integer that appears only once.
#
# You must implement a solution with O(n)O(n) runtime complexity and use only O(1)O(1) extra space.
#
# Input: nums = [3,2,3]
# Output: 2
#
# Input: nums = [7,6,6,7,8]
# Output: 8
####################

DEFAULT_BINARY_ARRAY_SIZE = 32

def singleNumber(nums):
    result = 0
    for n in nums:
        result = result ^ n
    return result

def main():
    print(singleNumber([3,2,3]))
    print(singleNumber([7,6,6,7,8]))

if __name__ == "__main__":
    main()