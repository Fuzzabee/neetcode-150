// You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
// 
// Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
// 
// Your solution must run in O(logn)O(logn) time.
// 
// Input: nums = [-1,0,2,4,6,8], target = 4
// Output: 3
// 
// Input: nums = [-1,0,2,4,6,8], target = 3
// Output: -1

#include <iostream>
#include <vector>

int search(std::vector<int>& nums, int target) {
    if (nums.size() == 0) { return -1; }

    int leftIndex = 0;
    int rightIndex = nums.size() - 1;

    while (rightIndex - leftIndex > 1) {
        int newIndex = (leftIndex + rightIndex) / 2;

        if (nums.at(newIndex) == target) { return newIndex; }
        if (nums.at(newIndex) < target) { leftIndex = newIndex + 1; }
        if (nums.at(newIndex) > target) { rightIndex = newIndex - 1; }
    }

    if (nums.at(leftIndex) == target) { return leftIndex; }
    if (nums.at(rightIndex) == target) { return rightIndex; }
    return -1;
}

void runTestSuite() {
    // Test 1
    std::vector<int> test1Nums = {-1, 0, 2, 4, 6, 8};
    int test1Target = 4;
    int test1Result = search(test1Nums, test1Target);
    std::cout << "Expected: 3 Actual: " << test1Result << "\n";

    // Test 2
    std::vector<int> test2Nums = {-1, 0, 2, 4, 6, 8};
    int test2Target = 3;
    int test2Result = search(test2Nums, test2Target);
    std::cout << "Expected: -1 Actual: " << test2Result << "\n";
}

int main() {
    runTestSuite();
    return 0;
}