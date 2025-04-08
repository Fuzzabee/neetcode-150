# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    # Singleton or empty
    if head == None or head.next == None:
        return head
    
    # Special case for first (new end) of the list
    previousNode = head
    currentNode = head.next
    head.next = None

    while currentNode != None:
        temp = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = temp

    return previousNode

def printList(head):
    list = []
    currentNode = head
    while currentNode != None:
        list.append(currentNode.val)
        currentNode = currentNode.next
    print(list)

def main():
    # Input: head = [0,1,2,3]
    # Output: [3,2,1,0]
    fourth = ListNode(3, None)
    third = ListNode(2, fourth)
    second = ListNode(1, third)    
    head = ListNode(0, second)
    printList(head)
    printList(reverseList(head))

    # Input: head = []
    # Output: []
    head = None
    printList(head)
    printList(reverseList(head))


if __name__ == "__main__":
    main()