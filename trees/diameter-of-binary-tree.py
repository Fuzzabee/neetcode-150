# The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.
# The length of a path between two nodes in a binary tree is the number of edges between the nodes.
# Given the root of a binary tree root, return the diameter of the tree.

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

############
# Solution #
############
def diameterOfBinaryTree(root):
    res = 0

    def dfs(node):
        nonlocal res

        if not node:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)
        res = max(res, left + right)

        return 1 + max(left, right)

    dfs(root)
    return res

        

def main():
    # Input: root = [1,null,2,3,4,5]
    # Output: 3
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    n1.right = n2
    n2.left = n3
    n2.right = n4
    n3.left = n5

    print(diameterOfBinaryTree(n1))

    # Input: root = [1,2,3]
    # Output: 2
    n1.left = n2
    n1.right = n3
    n2.left = None
    n2.right = None
    n3.left = None
    
    print(diameterOfBinaryTree(n1))


if __name__ == "__main__":
    main()