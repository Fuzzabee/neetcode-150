# You are given an integer array digits, where each digits[i] is the ith digit of a large integer. It is ordered from most significant to least significant digit, and it will not contain any leading zero.
# Return the digits of the given integer after incrementing it by one.

def plusOne(digits):
    # Check for if the number is all 9's, special case where we need to append
    allNines = True
    for n in digits:
        if n != 9:
            allNines = False
            break

    if allNines:
        result = [0] * (len(digits) + 1)
        result[0] = 1
        return result
    
    result = digits.copy()
    for i in range(len(result) - 1, -1, -1):
        if result[i] == 9:
            result[i] = 0
        else:
            result[i] += 1
            break

    return result


def main():
    # Input: digits = [1,2,3,4]
    # Output: [1,2,3,5]
    print(plusOne([1,2,3,4]))

    # Input: digits = [9,9,9]
    # Output: [1,0,0,0]
    print(plusOne([9,9,9]))

if __name__ == "__main__":
    main()