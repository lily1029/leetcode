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
    @param root: the root of binary tree.
    @return: An integer
    """
    def maxPathSum2(self, root):
        # 此题最直观的做法就是从root开始dfs到每个叶子结点
        #在这个过程中记录root值加上所有节点值一直到叶子节点值的和
        #这里用一个全局变量ans来track所有路径和的最大的值
        if not root:
            return 0 
        
        #全局变量
        ans = [-sys.maxsize]
        #这里进行从root到叶子节点的dfs
        self.dfs(root, 0, ans)
        return ans[0]

    #now_sum是记录从root到当前节点的sum和， ans是全局变量    
    def dfs(self, root, now_sum, ans):
        #当root为空时，返回
        if not root:
            return 
        
        #当递归一层时，更新now_sum值
        now_sum += root.val
        #并且更新全局变量值
        ans[0] = max(ans[0], now_sum)
        
        #dfs 左子树
        self.dfs(root.left, now_sum, ans)
        #dfs 右子树
        self.dfs(root.right, now_sum, ans)
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.maxPathSum2(root)
    print(x)





