// Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
// 
// Input: nums = [1, 2, 3, 3]
// Output: true
// 
// Input: nums = [1, 2, 3, 4]
// Output: false

#include <iostream>
#include <iterator>
#include <set>
#include <vector>

bool hasDuplicate(std::vector<int>& nums) {
    std::set<int> numsEncountered;
    std::vector<int>::iterator it;

    for (it = nums.begin(); it != nums.end(); ++it) {
        if (numsEncountered.find(*it) != numsEncountered.end()) {
            return true;
        }
        numsEncountered.insert(*it);
    }

    return false;
}

void runTestSuite() {
    std::vector<int> test1Input = {1, 2, 3, 3};
    int test1Result = hasDuplicate(test1Input);
    std::cout << "Expected: true Actual: " << test1Result << "\n";

    std::vector<int> test2Input = {1, 2, 3, 4};
    int test2Result = hasDuplicate(test2Input);
    std::cout << "Expected: false Actual: " << test2Result << "\n";    
}

int main() {
    runTestSuite();
    return 0;
}