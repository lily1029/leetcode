class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(5)
   
    node_1.left = node_2
    node_1.right = node_3

    node_2.right = node_4

    return node_1

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    
    # Method 1
    # def binaryTreePaths(self, root):
    #     # write your code here
    #     res = []
    #     def helper(root, cur):
    #         if not root:
    #             return 
    #         if not root.left and not root.right:
    #             res.append(cur + str(root.val))
            
    #         helper(root.left, cur + str(root.val) + "->")
    #         helper(root.right, cur + str(root.val) + "->")
    #     helper(root, "")
    #     return res
    """

    #Method 2: Divider Conquer 版本的 DFS
    def binary_tree_paths(self, root):
        # write your code here
        if root is None:
            return []
        # 99% 的题，不用单独处理叶子节点
        # 这里需要单独处理的原因是 root 是 None 的结果，没有办法用于构造 root 是叶子的结果
        if root.left is None and root.right is None:
            return [str(root.val)]
        
        #divide part分别拿到左右子树的路径
        leftPaths = self.binary_tree_paths(root.left)
        rightPaths = self.binary_tree_paths(root.right)

        paths = []

        for path in leftPaths + rightPaths:
            #conquer part, 将root 的值分别放到左右子树的路径最前面
            #构成整个数的所有路径
            #注意：不推荐用这种方法，时间更长因为[1] + [2, 5] = [1, 2, 5],产生了一个新的list
            #如果一个10000长的list + [1], 也会产生一个新的list,费时费空间，python中最好用.join(),时间是O(1)
            paths.append(str(root.val) + '->' + path)
        
        return paths   
    

    """
    # here we use dfs method, 这是最直观想到的一种方法，应该会写
    #最直观的做法就是dfs,从根结点开始一直往下走，直到找到一个叶子节点，这就是一条
    #合法路径，然后回溯过程中，陆续找到其它所有到叶子节点的所有路径
    def binaryTreePaths(self, root):
        if root is None:
            return []
            
        result = []
        self.dfs(root, [str(root.val)], result)
        return result

    def dfs(self, root, path, result):
        #这里找到叶子节点，所以把它join起来，成为一条从根结点到叶子节点的合法路径
        if root.left is None and root.right is None:
            result.append('->'.join(path))
            return

        #dfs 左子树，如果左子树不为空，append 左子树的节点，
        if root.left:
            path.append(str(root.left.val))
            #然后继续对左子树的左孩子进行dfs
            self.dfs(root.left, path, result)
            #此路径dfs后，backtracking, 返回上层
            path.pop()  # 回溯
        
        #dfs 右子树，如果右子树不为空，append 右子树的节点，
        if root.right:
            path.append(str(root.right.val))
            #然后继续对右子树的右孩子进行dfs
            self.dfs(root.right, path, result)
            #此路径dfs后，backtracking, 返回上层
            path.pop()
     """
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    # x = ll.binaryTreePaths(root)
    x =  ll.binary_tree_paths(root)
    
    print(x)


