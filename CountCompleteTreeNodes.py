class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.left =node_6 

    return node_1
class Solution:
    def countNodes(self, root):
        leftdepth = self.getdepth(root, True)
        rightdepth = self.getdepth(root, False)

        if leftdepth == rightdepth:
            return 2 ** leftdepth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def getdepth(self, root, isLeft):
        if root is None:
            return 0
        if isLeft:
            return 1 + self.getdepth(root.left, isLeft)
        else:
            return 1 + self.getdepth(root.right, isLeft)

if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.countNodes(root)
    print(x)
