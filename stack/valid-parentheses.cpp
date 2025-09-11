// You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
// 
// The input string s is valid if and only if:
// 
//     Every open bracket is closed by the same type of close bracket.
//     Open brackets are closed in the correct order.
//     Every close bracket has a corresponding open bracket of the same type.
// 
// Return true if s is a valid string, and false otherwise.
// 
// Input: s = "[]"
// Output: true
// 
// Input: s = "([{}])"
// Output: true
// 
// Input: s = "[(])"
// Output: false

#include <iostream>
#include <string>
#include <vector>

const std::string closingChars = "]})";

bool isValid(std::string s) {
    std::vector<char> stack;
    for (char c : s) {
        // If we have a close character but an empty stack, is not valid
        if (closingChars.find(c) != std::string::npos && stack.size() == 0) {
            return false;
        }

        // If we have a close character and something in the stack, ensure it matches
        if (closingChars.find(c) != std::string::npos) {
            if (stack.back() == '[' && c != ']') {
                return false;
            } else if (stack.back() == '{' && c != '}') {
                return false;
            } else if (stack.back() == '(' && c != ')') {
                return false;
            }
            stack.pop_back();
            continue;
        }

        stack.push_back(c);
    }
    return stack.empty();
}

void runTestSuite() {
    std::string test1Input = "[]";
    bool test1Result = isValid(test1Input);
    std::cout << "Expected: true (1) Actual: " << test1Result << "\n";

    std::string test2Input = "([{}])";
    bool test2Result = isValid(test2Input);
    std::cout << "Expected: true (1) Actual: " << test2Result << "\n";    

    std::string test3Input = "[(])";
    bool test3Result = isValid(test3Input);
    std::cout << "Expected: false (0) Actual: " << test3Result << "\n";  
}

int main() {
    runTestSuite();
    return 0;
}