# You are given an unsigned integer n. Return the number of 1 bits in its binary representation.
# You may assume n is a non-negative integer which fits within 32-bits.

def hammingWeight(n):
    totalOnes = 0
    for i in range (32):
        if n & (1 << i) != 0:
            totalOnes += 1

    return totalOnes

def main():
    # Input: n = 00000000000000000000000000010111
    # Output: 4
    print(hammingWeight(39))

    # Input: n = 01111111111111111111111111111101
    # Output: 30
    print(hammingWeight(2147483645))

if __name__ == "__main__":
    main()