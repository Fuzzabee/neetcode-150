# Given a binary tree, return true if it is height-balanced and false otherwise.
# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def makeQueue(nodes):
    newQueue = []
    for node in nodes:
        if node.left: newQueue.append(node.left)
        if node.right: newQueue.append(node.right)
    return newQueue

def getHeight(root):
    if not root: return 0

    queue = [root]
    height = 0
    while queue:
        queue = makeQueue(queue)
        height += 1
    return height


def isBalanced(root):
    if not root: return True

    leftHeight = getHeight(root.left)
    rightHeight = getHeight(root.right)
    return abs(leftHeight - rightHeight) <= 1

def main():
    # Input: root = [1,2,3,null,null,4]
    # Output: true
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    n1.left = n2
    n1.right = n3
    n3.left = n4

    print(isBalanced(n1))

    # Input: root = [1,2,3,null,null,4,null,5]
    # Output: false
    n4.left = n5
    print(isBalanced(n1))

    # Input: root = []
    # Output: true
    n1 = None
    print(isBalanced(n1))


if __name__ == "__main__":
    main()