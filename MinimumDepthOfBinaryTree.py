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

    node_1.left = node_2
    node_1.right = node_3

    node_3.left = node_4
    node_3.right = node_5

    return node_1
class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        if root is None:
            return 0
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        # 当左子树或右子树为空时，最小深度取决于另一颗子树
        if leftDepth == 0 or rightDepth == 0:
            return leftDepth + rightDepth + 1
        return min(leftDepth, rightDepth) + 1
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.minDepth(root)
    print(x)