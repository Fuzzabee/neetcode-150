# You are given a non-empty array of integers nums. Every integer appears twice except for one.
# Return the integer that appears only once.
# You must implement a solution with O(n)O(n) runtime complexity and use only O(1)O(1) extra space.

# Intuitive way for me, create a dictionary to store frequencies
# def singleNumber(nums):
#     frequencies = {}
#     for num in nums:
#         if num in frequencies:
#             frequencies[num] = frequencies[num] + 1
#         else:
#             frequencies[num] = 1

#     for num, frequency in frequencies.items():
#         if frequency == 1:
#             return num
#     return -1

# Bit manipulation. Since xor of n is 0, if we xor the whole list, the result
# will be the number that only appears once
def singleNumber(nums):
    result = 0
    for num in nums:
        result = result ^ num
    return result

def main():
    # Input: nums = [3,2,3]
    # Output: 2
    print(singleNumber([3,2,3]))

    # Input: nums = [7,6,6,7,8]
    # Output: 8
    print(singleNumber([7,6,6,7,8]))

if __name__ == "__main__":
    main()