class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(2)
   
    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4

    node_3.left = node_5

    return node_1

class Solution:
    #此题的做法和binarytreepathsum几乎一样，都是用dfs,区别在于
    #binarytreepathsum只是在root进行查找target,这道题是把树上
    #的每个点都可以当成一个新的根root进行向下查找，这里的find_path（）
    #函数和binarytreepathsum中的dfs()函数一摸一样，区别在于，当
    #完成根节点root后，继续对剩下的节点在调用这道题里的dfs（）函数
    def binaryTreePathSum2(self, root, target):
        result = []
    
        if root is None:
            return []
        
        # dfs this binary tree 
        self.dfs(root, target, result)
        return result
        
    def dfs(self, root, target, result):
        if not root:
            return
        
        # 具体怎样找到和target相等的paths
        self.find_path(root, 0, [], target, result)
        
        #左右递归，这里是把树上每个节点都当成一个新的根root进行dfs找
        #满足等于target的路径
        self.dfs(root.left, target, result)
        self.dfs(root.right, target, result)

    #此函数和binarytreepathsum中的dfs()函数完全一样    
    def find_path(self, root, now_sum, path, target, result):
        if not root:
            return
        
        #用now_sum 去记录当前节点的值
        now_sum += root.val
        #path 放路径
        path.append(root.val)
        
        if now_sum == target:
           result.append(path[:])
          
        self.find_path(root.left, now_sum, path, target, result)
        self.find_path(root.right, now_sum, path, target, result)
        
        #回溯
        path.pop()
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    target  = 6
    x = ll.binaryTreePathSum2(root, target)
  
    print(x)



