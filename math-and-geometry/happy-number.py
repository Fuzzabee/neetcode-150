# A non-cyclical number is an integer defined by the following algorithm:

#     Given a positive integer, replace it with the sum of the squares of its digits.
#     Repeat the above step until the number equals 1, or it loops infinitely in a cycle which does not include 1.
#     If it stops at 1, then the number is a non-cyclical number.

# Given a positive integer n, return true if it is a non-cyclical number, otherwise return false.

def isHappy(n):
    currentNum = n
    usedNums = []
    while currentNum > 1:
        if currentNum in usedNums: 
            return False
        
        usedNums.append(currentNum)
        
        newNum = 0
        while currentNum > 0:
            nextDigit = currentNum % 10
            newNum += nextDigit ** 2
            currentNum = currentNum // 10
        currentNum = newNum

    return True

def main():
    # Input: n = 100
    # Output: true
    print(isHappy(100))

    # Input: n = 101
    # Output: false
    print(isHappy(101))

if __name__ == "__main__":
    main()