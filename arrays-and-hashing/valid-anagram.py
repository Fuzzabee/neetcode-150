# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

def isAnagram(s, t):
    sAsList = list(s)
    for x in t:
        if x in sAsList:
            sAsList.remove(x)
        else:
            return False
    
    return len(sAsList) == 0

def main():
    # Input: s = "racecar", t = "carrace"
    # Output: true
    print(isAnagram("racecar", "carrace"))

    # Input: s = "jar", t = "jam"
    # Output: false
    print(isAnagram("jar", "jam"))

if __name__ == "__main__":
    main()