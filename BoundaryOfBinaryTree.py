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
   
    node_1.right = node_2

    node_2.left = node_3
    node_2.right = node_4

    return node_1
class Solution:
    """
    最简单直接的思路就是进行三次DFS, 分别对左边界DFS, 叶子节点DFS, 右边界DFS放到答案序列中.
    """
    def boundaryOfBinaryTree(self, root):
        self.ans = []
        if root == None:
            return self.ans
        #答案需要第一个点是root
        self.ans.append(root.val)
        #如果只有一个点，我们判断这个点左右孩子为空，然后返回
        if root.left == None and root.right == None:
            return self.ans
        self.dfsLeft(root.left)
        self.dfsLeaf(root)
        self.dfsRight(root.right)
        return self.ans
    #左边界DFS: 从根的左孩子节点开始, 优先向左, 没有左孩子节点就向右, 直到叶子节点, 沿路的所有节点放入答案序列
    def dfsLeft(self, rt):
        if rt == None or (rt.left == None and rt.right == None):
            return
        self.ans.append(rt.val)
        if rt.left != None:
            self.dfsLeft(rt.left)
        else:
            self.dfsLeft(rt.right)
    #DFS下面叶子节点: 遍历整棵树, 为了保证逆时针顺序, 需要先访问左孩子节点, 碰到叶子就放入答案序列   
    def dfsLeaf(self, rt):
        if rt == None:
            return 
      # if rt.left == None and rt.right == None: 这2种写法都可以
        if not rt.left and not rt.right:
            self.ans.append(rt.val)
            return
        self.dfsLeaf(rt.left)
        self.dfsLeaf(rt.right)
    #DFS右边界: 与左边界类似, 只不过将节点放入答案序列的时机要延后 -- 在递归结束时放入
    def dfsRight(self, rt):
        if rt == None or (rt.left == None and rt.right == None):
            return
        if rt.right != None:
            self.dfsRight(rt.right)
        else:
            self.dfsRight(rt.left)
        self.ans.append(rt.val)

if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.boundaryOfBinaryTree(root)
    print(x)
