### INSTRUCTIONS ###
# You are given an unsigned integer n. Return the number of 1 bits in its binary representation.
#
# You may assume n is a non-negative integer which fits within 32-bits.
#
# Input: n = 00000000000000000000000000010111
# Output: 4
#
# Input: n = 01111111111111111111111111111101
# Output: 30
####################

def hammingWeight(n):
    result = 0
    while (n):
        result += (n & 1) # Takes least sig byte from n and ands with 1
        n >>= 1 # Bit shift right to get next sig bit
    return result

def main():
    print(hammingWeight(23))
    print(hammingWeight(2147483645))

if __name__ == "__main__":
    main()