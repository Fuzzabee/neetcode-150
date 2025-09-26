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
    if (root == nullptr) {
        std::cout << "[]\n";
        return;
    }

    std::vector<TreeNode*> queue = {root};

    std::cout << "[";
    while (queue.size() != 0) {
        std::vector<TreeNode*> newQueue;
        for (TreeNode* curNode : queue) {
            if (curNode->left != nullptr) { newQueue.push_back(curNode->left); }
            if (curNode->right != nullptr) { newQueue.push_back(curNode->right); }

            std::cout << curNode->val << ",";
        }
        queue = newQueue;
    }
    std::cout << "]\n";
}

TreeNode* invertTree(TreeNode* root) {
    if (root == nullptr) { return root; }

    std::vector<TreeNode*> queue = {root};
    while (queue.size() != 0) {
        std::vector<TreeNode*> newQueue;
        for (TreeNode* curNode : queue) {
            if (curNode->left != nullptr) { newQueue.push_back(curNode->left); }
            if (curNode->right != nullptr) { newQueue.push_back(curNode->right); }
            TreeNode* temp = curNode->left;
            curNode->left = curNode->right;
            curNode->right = temp;
        }
        queue = newQueue;
    }

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
    test1Node2.right = &test1Node5;
    test1Node3.left = &test1Node6;
    test1Node3.right = &test1Node7;

    std::cout << "Test 1 Input: ";
    printTree(&test1Node1);
    invertTree(&test1Node1);
    std::cout << "Test 1 Output: ";
    printTree(&test1Node1);

    // Test 2
    TreeNode test2Node1 = TreeNode(3);
    TreeNode test2Node2 = TreeNode(2);
    TreeNode test2Node3 = TreeNode(1);
    
    test2Node1.left = &test2Node2;
    test2Node1.right = &test2Node3;

    std::cout << "Test 2 Input: ";
    printTree(&test2Node1);
    invertTree(&test2Node1);
    std::cout << "Test 2 Output: ";
    printTree(&test2Node1);
    
    // Test 3
    TreeNode* test3Node1 = nullptr;

    std::cout << "Test 3 Input: ";
    printTree(test3Node1);
    invertTree(test3Node1);
    std::cout << "Test 3 Output: ";
    printTree(test3Node1);
}

int main() {
    runTestSuite();
    return 0;
}