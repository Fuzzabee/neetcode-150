# Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
# There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.
# Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.
# Note: index is not given to you as a parameter.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    visited = set()
    currentNode = head
    while currentNode:
        if currentNode in visited:
            return True
        visited.add(currentNode)
        currentNode = currentNode.next
    return False

def main():
    # Input: head = [1,2,3,4], index = 1
    # Output: true
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2

    print(hasCycle(n1))

    # Input: head = [1,2], index = -1
    # Output: false
    n1.next = n2
    n2.next = None

    print(hasCycle(n1))

if __name__ == "__main__":
    main()