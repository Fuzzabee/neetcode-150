### INSTRUCTIONS ###
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#
# Return the answer with the smaller index first.
#
# nums = [3,4,5,6], target = 7
# Output: [0,1]
#
# Input: nums = [4,5,6], target = 10
# Output: [0,2]
#
# Input: nums = [5,5], target = 10
# Output: [0,1]
####################

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if not head: return False
    visitedNodes = set()
    currentNode = head
    while currentNode:
        if currentNode in visitedNodes: return True
        visitedNodes.add(currentNode)
        currentNode = currentNode.next
    return False

def main():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    print(hasCycle(n1))

    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    print(hasCycle(n1))

if __name__ == "__main__":
    main()