import sys


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    
    node_1.left = node_2
    node_1.right = node_3

    return node_1
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):

        #此题的解法是用divide and conquer method
        #max是一个全局变量，找整棵树最大值
        #先算出来左子树的最大值，在算出右子树的最大值，然后在
        #找出 max（左子树最大值， 右子树最大值，左子树最大值+右子树最大值+root)
        #中的最大值

        #这里是全局变量track最大值
        self.max = -sys.maxsize - 1

        #调用divide and conquer method
        self.helper(root)

        return self.max 
    
    def helper(self, root):
        #if the root is none, return 0
        if not root:
            return 0 
        
        #divide part, 算左子树的值
        left_sum = self.helper(root.left)
        #这里leftSum <= 0时，表示我们就不要这条路上的权值了，因为题目是找大值
        if left_sum <= 0:
            left_sum = 0 
        
        #divide part, 算右子树的值
        right_sum = self.helper(root.right)
        if right_sum <= 0:
            right_sum = 0 
        
        #全局找最大值，其中左子树值+root节点值+右子树值也是一条合法路径
        #conquer part并找出最大值
        self.max = max(self.max, left_sum + root.val + right_sum)

        #这里返回的是以这个root为根的，左子树+root的最大值，或是右子树+root的最大值
        return max(left_sum + root.val, right_sum + root.val)
    
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.maxPathSum(root)
    print(x)






