// Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
// 
// Input: head = [0,1,2,3]
// Output: [3,2,1,0]
// 
// Input: head = []
// Output: []

#include <iostream>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

void printList(ListNode* head) {
    ListNode* curNode = head;

    std::cout << "[";
    while (curNode != nullptr) {
        std::cout << curNode->val;
        curNode = curNode->next;
        if (curNode != nullptr) {
            std::cout << ",";
        }        
    }
    std::cout << "]\n";
}

ListNode* reverseList(ListNode* head) {
    if (head == nullptr) { return head; }

    ListNode* curNode = head;
    ListNode* prevNode = nullptr;
    while (curNode->next != nullptr) {
        ListNode* nextNode = curNode->next;
        curNode->next = prevNode;
        prevNode = curNode;
        curNode = nextNode;
    }
    curNode->next = prevNode;

    return curNode;
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