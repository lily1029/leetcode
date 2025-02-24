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
        #此题做法是:如果想知道the shortest path among all the paths 
        #from root to leaf, 可以用divide and conquer method
        #分别找出root下的左子树的shortest path, 在找出右子树的shortest path,
        #然后挑出左右子树中最小的shortest path 在加上root这个节点，就是整棵树的
        #shortest path

        #divide parts
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)

        # 当左子树或右子树为空时，最小深度取决于另一颗子树
        if leftDepth == 0 or rightDepth == 0:
            return leftDepth + rightDepth + 1
        
        #这里找出整棵树的最小值来自于左子树或是右子树，然后加上root 根节点就是整棵树的 shortest path
        #conquer part
        return min(leftDepth, rightDepth) + 1
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.minDepth(root)
    print(x)