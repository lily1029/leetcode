import sys
from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(-5)
    node_3 = TreeNode(2)
    node_4 = TreeNode(1)
    node_5 = TreeNode(2)
    node_6 = TreeNode(-4)
    node_7 = TreeNode(-5)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    return node_1

class Solution:

    def findSubtree(self, root):
        minimum, subtree, sum_of_root = self.helper(root)
        return subtree

    def helper(self, root):
        if root is None:
            return sys.maxsize, None, 0

        #Divide Parts
        #leftMinimum means:左子树的最小值，leftSubtree：左子树的根，leftSum 左边子树的和 
        leftMinimum, leftSubtree, leftSum = self.helper(root.left)
        #rightSubtree means:右子树的最小值，rightSubtree：右子树的根rightSum 右边子树的和 
        rightMinimum, rightSubtree, rightSum = self.helper(root.right)
        
        #conquer 求sum_of_root的值是求以root为根的这个subtree的值是多少
        sum_of_root = leftSum + rightSum + root.val

        
        #如果minimum subtree是左子树，就返回 leftMinimum, leftSubtree, sum_of_root
        if leftMinimum == min(leftMinimum, rightMinimum, sum_of_root):
            return leftMinimum, leftSubtree, sum_of_root
        #如果minimum subtree是右子树，就返回 rightMinimum, rightSubtree, sum_of_root
        if rightMinimum == min(leftMinimum, rightMinimum, sum_of_root):
            return rightMinimum, rightSubtree, sum_of_root
        #这种情况的minimum subtree即不在左子树也不在右子树，而在以root为根的这个tree是最小的minimum subtree
        return sum_of_root, root, sum_of_root
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.findSubtree(root)
    print(x.val)