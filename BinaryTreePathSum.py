class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(4)
    node_4 = TreeNode(2)
    node_5 = TreeNode(3)
   
    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    return node_1

class Solution:
    #此道题的做法就是从root开始对所有叶子节点进行dfs，在走到叶子节点时，
    #算整个路径上的节点的sum，如果sum值等于target,放入到result中，
    #走完一条到叶子节点的路径后，要做backtracking, 弹出叶子节点，继续
    #走向下一个叶子节点
    
    def binaryTreePathSum(self, root, target):
        # 存放最终符合条件的路径
        result = []
        #保存每条路径的variable
        path = []
        #进行dfs
        self.dfs(root, path, result, 0,  target)

        return result

    #len varaiable 算路径的sum
    def dfs(self, root, path, result, len, target):
        #corner case
        if root is None:
            return

        #path 保存每条路径的节点
        path.append(root.val)
        #算路径的sum
        len += root.val

        #走到叶子节点，并判断是否sum等于target,如果等于， 全部放入result中
        if root.left is None and root.right is None and len == target:
            result.append(path[:])

        #dfs左子树
        self.dfs(root.left, path, result, len, target)
        #dfs右子树
        self.dfs(root.right, path, result, len, target)

        #backtracking
        path.pop()
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    target  = 5
    x = ll.binaryTreePathSum(root, target)
  
    print(x)


