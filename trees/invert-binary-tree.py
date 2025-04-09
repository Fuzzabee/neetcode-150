# You are given the root of a binary tree root. Invert the binary tree and return its root.

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

def invertTree(root):
    if root == None:
        return
    invert([root])
    return root
    
def invert(nodesToInvert):
    if not nodesToInvert: return
    curNode = nodesToInvert.pop(0)
    if curNode.left != None:
        nodesToInvert.append(curNode.left)
    if curNode.right != None:
        nodesToInvert.append(curNode.right)
    temp = curNode.left
    curNode.left = curNode.right
    curNode.right = temp
    invert(nodesToInvert)


def printTreeAsList(root):
    if root == None:
        return
    
    queue = [root]
    nodeList = []
    while queue:
        curNode = queue.pop(0)
        nodeList.append(curNode.val)
        if curNode.left != None:
            queue.append(curNode.left)
        if curNode.right != None:
            queue.append(curNode.right)
    print(nodeList)

def main():
    # Input: root = [1,2,3,4,5,6,7]
    # Output: [1,3,2,7,6,5,4]
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    printTreeAsList(a)
    printTreeAsList(invertTree(a))

    # Input: root = [3,2,1]
    # Output: [3,1,2]
    c.left = b
    c.right = a
    a.left = None
    a.right = None
    b.left = None
    b.right = None
    printTreeAsList(c)
    printTreeAsList(invertTree(c))

    # Input: root = []
    # Output: 
    a = None
    printTreeAsList(a)
    printTreeAsList(invertTree(a))

if __name__ == "__main__":
    main()