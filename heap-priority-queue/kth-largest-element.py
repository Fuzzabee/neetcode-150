### INSTRUCTIONS ###
# Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.
#
# Implement the following methods:
#
#     constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
#     int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.
#
# Input:
# ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]
#
# Output:
# [null, 3, 3, 3, 5, 6]
#
# Explanation:
# KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);
# kthLargest.add(3);   // return 3
# kthLargest.add(5);   // return 3
# kthLargest.add(6);   // return 3
# kthLargest.add(7);   // return 5
# kthLargest.add(8);   // return 6
####################

class KthLargest:
    def __init__(self, k, nums):
        self.target = k
        self.elements = nums
        self.elements.sort()

    # The use of sort is pretty worthless, we can find the index and insert it with better time, but makes the
    # code less readable. If we needed efficiency, would use binary search for faster insertion
    def add(self, val):
        self.elements.append(val)
        self.elements.sort()
        return self.elements[(-1 * self.target)]

def main():
    kthLargest = KthLargest(3, [1,2,3,3])
    print(kthLargest.add(3))
    print(kthLargest.add(5))
    print(kthLargest.add(6))
    print(kthLargest.add(7))
    print(kthLargest.add(8))

if __name__ == "__main__":
    main()