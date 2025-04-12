# Given the root of a binary tree, return its depth.
# The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

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

def maxDepth(root):
    if not root: return 0
    return calculateDepth([root], 0)

def calculateDepth(queue, depth):
    if not queue:
        return depth
    depth += 1
    newQueue = []
    while queue:
        nextNode = queue.pop()
        if nextNode.left:
            newQueue.append(nextNode.left)
        if nextNode.right:
            newQueue.append(nextNode.right)
    return calculateDepth(newQueue, depth)

def main():
    # Input: root = [1,2,3,null,null,4]
    # Output: 3
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n1.left = n2
    n1.right = n3
    n3.left = n4
    print(maxDepth(n1))

    # Input: root = [1,null,2]
    # Output: 2
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n1.right = n2
    print(maxDepth(n1))

    # Input: root = [0]
    # Output: 1
    n1 = TreeNode(0)
    print(maxDepth(n1))

    # Input: root = []
    # Output: 0
    n1 = None
    print(maxDepth(n1))

if __name__ == "__main__":
    main()