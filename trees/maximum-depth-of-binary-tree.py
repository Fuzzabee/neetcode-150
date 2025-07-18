### INSTRUCTIONS ###
# Given the root of a binary tree, return its depth.
#
# The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Input: root = [1,2,3,null,null,4]
# Output: 3
#
# Input: root = []
# Output: 0
####################

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTreeAsArray(root):
    if not root:
        print("[]")
        return
    result = []
    queue = [root]
    while queue:
        isOnlyNull = True
        newQueue = []
        for n in queue:
            if n:
                isOnlyNull = False
                result.append(n.val)
                newQueue.append(n.left)
                newQueue.append(n.right)
            else:
                result.append(None)
        if isOnlyNull:
            break
        queue = newQueue

    print(result)
    return

def maxDepth(root):
    if not root: return 0
    curDepth = 0
    queue = [root]
    while queue:
        curDepth += 1
        newQueue = []
        for n in queue:
            if n.left: newQueue.append(n.left)
            if n.right: newQueue.append(n.right)
        queue = newQueue
    return curDepth

def main():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n1.left = n2
    n1.right = n3
    n3.left = n4

    print(maxDepth(n1))
    print(maxDepth(None))

if __name__ == "__main__":
    main()