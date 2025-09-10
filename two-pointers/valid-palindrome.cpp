// Given a string s, return true if it is a palindrome, otherwise return false.
// 
// A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
// 
// Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
// 
// Input: s = "Was it a car or a cat I saw?"
// Output: true
// 
// Input: s = "tab a cat"
// Output: false

#include <iostream>
#include <string>

std::string onlyAlphaNum(std::string s) {
    std::string returnString = "";
    for (char c : s) {
        if (std::isalnum(c)) {
            returnString.append(1, c);
        }
    }
    return returnString;
}

bool isPalindrome(std::string s) {
    std::string sModified = onlyAlphaNum(s);
    int leftIndex = 0;
    int rightIndex = sModified.length() - 1;

    while (leftIndex < rightIndex) {
        if (std::tolower(sModified.at(leftIndex)) != std::tolower(sModified.at(rightIndex))) {
            return false;
        }
        ++leftIndex;
        --rightIndex;
    }
    return true;
}

void runTestSuite() {
    std::string test1Input = "Was it a car or a cat I saw?";
    int test1Result = isPalindrome(test1Input);
    std::cout << "Expected: true (1) Actual: " << test1Result << "\n";

    std::string test2Input = "tab a cat";
    int test2Result = isPalindrome(test2Input);
    std::cout << "Expected: false (0) Actual: " << test2Result << "\n";    
}

int main() {
    runTestSuite();
    return 0;
}