// You are given the root of a binary tree root. Invert the binary tree and return its root.
// 
// Input: root = [1,2,3,4,5,6,7]
// Output: [1,3,2,7,6,5,4]
// 
// Input: root = [3,2,1]
// Output: [3,1,2]
// 
// Input: root = []
// Output: []

#include <iostream>

// Definition for a binary tree node.
 struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

void printTree(TreeNode* root) {
    return;
}

TreeNode* invertTree(TreeNode* root) {
    return root;
}

void runTestSuite() {
    // Test 1
    ListNode test1Node0 = ListNode(0);
    ListNode test1Node1 = ListNode(1);
    ListNode test1Node2 = ListNode(2);
    ListNode test1Node3 = ListNode(3);

    test1Node0.next = &test1Node1;
    test1Node1.next = &test1Node2;
    test1Node2.next = &test1Node3;

    // printList(&test1Node0);

    ListNode* test1Result = reverseList(&test1Node0);
    std::cout << "Expected: [3,2,1,0] Actual: ";
    printList(test1Result);
    std::cout << "\n";

    // Test 2
    ListNode* test2Node1 = nullptr;
    ListNode* test2Result = reverseList(test2Node1);
    std::cout << "Expected: [] Actual: ";
    printList(test2Result);
}

int main() {
    runTestSuite();
    return 0;
}