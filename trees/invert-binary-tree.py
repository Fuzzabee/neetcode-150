### INSTRUCTIONS ###
# You are given the root of a binary tree root. Invert the binary tree and return its root.
#
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,3,2,7,6,5,4]
#
# Input: root = [3,2,1]
# Output: [3,1,2]
#
# Input: root = []
# Output: []
####################

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convertTreeToList(root):
    if not root: return []

    result = []
    queue = [root]

    while queue:
        newQueue = []
        for n in queue:
            result.append(n.val)
            if n.left: newQueue.append(n.left)
            if n.right: newQueue.append(n.right)
        queue = newQueue
    return result

def invertTree(root):
    if not root: return root

    queue = [root]

    while queue:
        newQueue = []
        for n in queue:
            temp = n.left
            n.left = n.right
            n.right = temp
            if n.left: newQueue.append(n.left)
            if n.right: newQueue.append(n.right)
        queue = newQueue
    return root

def main():
    n0 = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(3)
    n3 = TreeNode(4)
    n4 = TreeNode(5)
    n5 = TreeNode(6)
    n6 = TreeNode(7)

    n0.left = n1
    n0.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right = n6

    print(convertTreeToList(invertTree(n0)))

    n0 = TreeNode(3)
    n1 = TreeNode(2)
    n2 = TreeNode(1)

    n0.left = n1
    n0.right = n2

    print(convertTreeToList(invertTree(n0)))

    print(convertTreeToList(invertTree(None)))

if __name__ == "__main__":
    main()