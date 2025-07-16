### INSTRUCTIONS ###
# A non-cyclical number is an integer defined by the following algorithm:
#
#     Given a positive integer, replace it with the sum of the squares of its digits.
#     Repeat the above step until the number equals 1, or it loops infinitely in a cycle which does not include 1.
#     If it stops at 1, then the number is a non-cyclical number.
#
# Given a positive integer n, return true if it is a non-cyclical number, otherwise return false.
#
# Input: n = 100
# Output: true
#
# Input: n = 101
# Output: false
####################

def isHappy(n):
    seenNums = set()
    currentNum = n
    while currentNum != 1:
        newNum = 0
        slicedNum = currentNum
        while slicedNum >= 10:
            newNum += (slicedNum % 10) ** 2
            slicedNum = slicedNum // 10
        newNum += slicedNum ** 2
        if newNum in seenNums: return False
        seenNums.add(newNum)
        currentNum = newNum
    return True

def main():
    print(isHappy(100))
    print(isHappy(101))
    print(isHappy(7))

if __name__ == "__main__":
    main()