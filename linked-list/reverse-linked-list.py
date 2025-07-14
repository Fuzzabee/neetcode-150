### INSTRUCTIONS ###
# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
#
# Input: head = [0,1,2,3]
# Output: [3,2,1,0]
#
# Input: head = []
# Output: []
####################

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printNodeList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def reverseList(head):
    curNode = head
    prevNode = None

    while curNode:
        nextNode = curNode.next
        curNode.next = prevNode
        prevNode = curNode
        curNode = nextNode

    if head: head.next = None
    return prevNode

def main():
    node4 = ListNode(3)
    node3 = ListNode(2, node4)
    node2 = ListNode(1, node3)
    node1 = ListNode(0, node2)
    print(printNodeList(reverseList(node1)))
    print(printNodeList(reverseList(None)))


if __name__ == "__main__":
    main()