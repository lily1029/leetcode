class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 =  TreeNode(4)
    node_5 = TreeNode(5)
    
    node_1.left = node_2
    node_1.right = node_3

    node_3.left = node_4
    node_3.right = node_5

    return node_1

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    #此道题用divide and conquer method,先算出左子树的max depth
    #在算出右子树的max depth, 然后找出左右子树中最大的max depth, 然后+1是root整棵树的max depth
    #The maximum depth is the number of nodes along the longest path from the root 
    #node down to the farthest leaf node.
    def maxDepth(self, root):
        # corner case
        if not root:
            return 0 
        
        #divide part, 算出左子树的 max  depth
        leftSubTree = self.maxDepth(root.left)
        #算出右子树的max depth
        rightSubTree = self.maxDepth(root.right)
        
        #conquer part, 左右子树选出最大的然后+ 1 （root 高度）
        return max(leftSubTree, rightSubTree) + 1
    
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()

    x = ll.maxDepth(root)
    print(x) 
    
    
