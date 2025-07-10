### INSTRUCTIONS ###
# Given a string s, return true if it is a palindrome, otherwise return false.
#
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
#
# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
#
# Input: s = "Was it a car or a cat I saw?"
# Output: true
#
# Input: s = "tab a cat"
# Output: false
####################

def isPalindrome(s):
    leftIndex = 0
    rightIndex = len(s) - 1

    while leftIndex < rightIndex:
        if not s[leftIndex].isalnum():
            leftIndex += 1
            continue
        if not s[rightIndex].isalnum():
            rightIndex -= 1
            continue
        if not s[rightIndex].lower() == s[leftIndex].lower():
            return False
        leftIndex += 1
        rightIndex -= 1

    return True

def main():
    print(isPalindrome("Was it a car or a cat I saw?"))
    print(isPalindrome("tab a cat"))
    print(isPalindrome("0P"))

if __name__ == "__main__":
    main()