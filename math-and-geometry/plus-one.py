### INSTRUCTIONS ###
# You are given an integer array digits, where each digits[i] is the ith digit of a large integer. It is ordered from most significant to least significant digit, and it will not contain any leading zero.
#
# Return the digits of the given integer after incrementing it by one.
#
# Input: digits = [1,2,3,4]
# Output: [1,2,3,5]
#
# Input: digits = [9,9,9]
# Output: [1,0,0,0]
####################

def plusOne(digits):
    result = digits.copy()
    for i in range(len(result) - 1, 0, -1):
        if result[i] != 9:
            result[i] += 1
            return result
        result[i] = 0

    if result[0] == 9:
        result[0] = 0
        result.insert(0, 1)
    else:
        result[0] += 1
    return result

def main():
    print(plusOne([1,2,3,4]))
    print(plusOne([9,9,9]))

if __name__ == "__main__":
    main()