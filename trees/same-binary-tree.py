# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
# Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    pQueue = [p]
    qQueue = [q]

    while pQueue and qQueue:
        newPQueue = []
        newQQueue = []
        for i in range(len(pQueue)):
            pNode = pQueue[i]
            qNode = qQueue[i]
            print(pNode.val, qNode.val)
            if (not pNode) and (not qNode):
                continue
            if not pNode.left and not pNode.right and not qNode.left and not qNode.right:
                continue
            if (not pNode.left and qNode.left) or (pNode.left and not qNode.left) or (not pNode.right and qNode.right) or (pNode.right and not qNode.right):
                return False
            if (pNode.left.val != qNode.left.val) or (pNode.right.val != qNode.right.val):
                return False
            newPQueue.append(pNode.left)
            newPQueue.append(pNode.right)
            newQQueue.append(qNode.left)
            newQQueue.append(qNode.right)
        
        pQueue = newPQueue
        qQueue = newQQueue
    return True

def main():
    # Input: p = [1,2,3], q = [1,2,3]
    # Output: true
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3

    n4 = TreeNode(1)
    n5 = TreeNode(2)
    n6 = TreeNode(3)
    n4.left = n5
    n4.right = n6

    print(isSameTree(n1, n4))

    # Input: p = [4,7], q = [4,null,7]
    # Output: false
    n1 = TreeNode(4)
    n2 = TreeNode(7)
    n1.left = n2

    n3 = TreeNode(4)
    n4 = TreeNode(7)
    n3.right = n4

    print(isSameTree(n1, n3))

    # Input: p = [1,2,3], q = [1,3,2]
    # Output: false
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3

    n4 = TreeNode(1)
    n5 = TreeNode(3)
    n6 = TreeNode(2)
    n4.left = n5
    n4.right = n6
    print(isSameTree(n1, n4))

if __name__ == "__main__":
    main()