# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
# The new list should be made up of nodes from list1 and list2.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printAsList(head):
    currentNode = head
    nodeList = []
    while currentNode:
        nodeList.append(currentNode.val)
        currentNode = currentNode.next
    print(nodeList)

def mergeTwoLists(list1, list2):
    if not list1 and not list2:
        return None
    if not list1:
        return list2
    if not list2:
        return list1
    
    head = list1 if list1.val < list2.val else list2
    curList1 = list1.next if list1.val < list2.val else list1
    curList2 = list2.next if list1.val >= list2.val else list2
    lastInserted = head

    while curList1 or curList2:
        if not curList1:
            lastInserted.next = curList2
            break
        elif not curList2:
            lastInserted.next = curList1
            break
        else:
            if curList1.val < curList2.val:
                nextNode = curList1.next
                lastInserted.next = curList1
                lastInserted = lastInserted.next
                curList1 = nextNode
            else:
                nextNode = curList2.next
                lastInserted.next = curList2
                lastInserted = lastInserted.next
                curList2 = nextNode
    
    return head


def main():
    # Input: list1 = [1,2,4], list2 = [1,3,5]
    # Output: [1,1,2,3,4,5]
    list1Item1 = ListNode(1)
    list1Item2 = ListNode(2)
    list1Item3 = ListNode(4)
    list1Item1.next = list1Item2
    list1Item2.next = list1Item3

    list2Item1 = ListNode(1)
    list2Item2 = ListNode(3)
    list2Item3 = ListNode(5)
    list2Item1.next = list2Item2
    list2Item2.next = list2Item3

    printAsList(mergeTwoLists(list1Item1, list2Item1))

    # Input: list1 = [], list2 = [1,2]
    # Output: [1,2]
    list1Item1 = None
    list2Item1 = ListNode(1)
    list2Item2 = ListNode(2)

    list2Item1.next = list2Item2

    printAsList(mergeTwoLists(list1Item1, list2Item1))

    # Input: list1 = [], list2 = []
    # Output: []
    list1Item1 = None
    list2Item1 = None

    printAsList(mergeTwoLists(list1Item1, list2Item1))


if __name__ == "__main__":
    main()