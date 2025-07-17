### INSTRUCTIONS ###
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
#
# The new list should be made up of nodes from list1 and list2.
#
# Input: list1 = [1,2,4], list2 = [1,3,5]
# Output: [1,1,2,3,4,5]
#
# Input: list1 = [], list2 = [1,2]
# Output: [1,2]
#
# Input: list1 = [], list2 = []
# Output: []
####################

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def convertListToListNode(list):
    if not list: return None
    result = []
    for n in list:
        result.append(ListNode(n))
    for i in range(len(result) - 1):
        result[i].next = result[i + 1]

    return result[0]

def printListFromNode(head):
    if not head:
        print("[]")
        return
    result = [head.val]
    currentNode = head.next
    while currentNode:
        result.append(currentNode.val)
        currentNode = currentNode.next
    print(result)
    return None

def mergeTwoLists(list1, list2):
    if not list1: return list2
    if not list2: return list1
    result = []
    curList1 = list1
    curList2 = list2
    while curList1 or curList2:
        if not curList1:
            result.append(curList2.val)
            curList2 = curList2.next
        elif not curList2:
            result.append(curList1.val)
            curList1 = curList1.next
        else:
            if curList1.val < curList2.val:
                result.append(curList1.val)
                curList1 = curList1.next
            else:
                result.append(curList2.val)
                curList2 = curList2.next

    return convertListToListNode(result)

def main():
    l1 = convertListToListNode([1,2,4])
    l2 = convertListToListNode([1,3,5])
    printListFromNode(mergeTwoLists(l1, l2))

if __name__ == "__main__":
    main()