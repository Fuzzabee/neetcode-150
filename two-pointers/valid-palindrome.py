import re # For regex

# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

def isPalindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower() # Get only alphanumerics and digits
    left = 0
    right = len(s) - 1

    while (left < right):
        # print("Testing left: " + s[left] + " and right: " + s[right])
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True 

def main():
    # Input: s = "Was it a car or a cat I saw?"
    # Output: true
    s = "Was it a car or a cat I saw?"
    print(isPalindrome(s))

    # Input: s = "tab a cat"
    # Output: false
    s = "tab a cat"
    print(isPalindrome(s))

if __name__ == "__main__":
    main()