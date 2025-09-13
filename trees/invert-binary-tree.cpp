// Input: root = [1,2,3,4,5,6,7]
// Output: [1,3,2,7,6,5,4]
// 
// Input: root = [3,2,1]
// Output: [3,1,2]
// 
// Input: root = []
// Output: []

#include <iostream>
#include <vector>

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
    std::vector<TreeNode*> queue = {root};

    std::cout << "[";
    while (queue.size() != 0) {
        std::vector<TreeNode*> newQueue;
        for (TreeNode* curNode : queue) {
            if (curNode->left == nullptr && curNode->right == nullptr) { continue; }
            if (curNode->left != nullptr) { newQueue.push_back(curNode->left); }
            if (curNode->right != nullptr) { newQueue.push_back(curNode->right); }

            std::cout << curNode->val << ",";
        }
        queue = newQueue;
    }
    std::cout << "]\n";
}

TreeNode* invertTree(TreeNode* root) {
    return root;
}

void runTestSuite() {
    // Test 1
    TreeNode test1Node1 = TreeNode(1);
    TreeNode test1Node2 = TreeNode(2);
    TreeNode test1Node3 = TreeNode(3);
    TreeNode test1Node4 = TreeNode(4);
    TreeNode test1Node5 = TreeNode(5);
    TreeNode test1Node6 = TreeNode(6);
    TreeNode test1Node7 = TreeNode(7);
    
    test1Node1.left = &test1Node2;
    test1Node1.right = &test1Node3;
    test1Node2.left = &test1Node4;
    test1Node2.left = &test1Node5;
    test1Node3.left = &test1Node6;
    test1Node3.left = &test1Node7;

    printTree(&test1Node1);

    // ListNode* test1Result = reverseList(&test1Node0);
    // std::cout << "Expected: [3,2,1,0] Actual: ";
    // printList(test1Result);
    // std::cout << "\n";

    // Test 2
    // ListNode* test2Node1 = nullptr;
    // ListNode* test2Result = reverseList(test2Node1);
    // std::cout << "Expected: [] Actual: ";
    // printList(test2Result);
}

int main() {
    runTestSuite();
    return 0;
}