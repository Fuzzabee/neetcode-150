// Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.
// 
// Implement the following methods:
// 
//     constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
//     int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.
// 
// Input:
// ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]
// 
// Output:
// [null, 3, 3, 3, 5, 6]

#include <algorithm>
#include <iostream>
#include <list>
#include <vector>

class KthLargest {
private:
    int k;
    std::list<int> nums;

    std::list<int> getKFromList(int k, std::vector<int>& nums) {
        std::list<int> returnList(k, 0);
        for (int n : nums) {
            if (n <= returnList.back()) {
                continue;
            }
        }

        return returnList;
    }
public:
    KthLargest(int k, std::vector<int>& nums) {
        this->k = k;
        this->nums = getKFromList(k, nums);
        for (int n : this->nums) {
            std::cout << n << "\n";
        }
    }
    
    int add(int val) {
        return 0;
    }
};

void runTestSuite() {
    std::vector<int> test1Stream = {1,2,3,3};
    KthLargest test1(3, test1Stream);
}

int main() {
    runTestSuite();
    return 0;
}