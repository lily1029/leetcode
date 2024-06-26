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
    @param root: a TreeNode
    @return: a list of integer
    """
    def boundaryOfBinaryTree(self, root):
        self.ans = []
        if root == None:
            return self.ans
        self.ans.append(root.val)
        if root.left == None and root.right == None:
            return self.ans
        self.dfsLeft(root.left)
        self.dfsLeaf(root)
        self.dfsRight(root.right)
        return self.ans
    
    def dfsLeft(self, rt):
        if rt == None or (rt.left == None and rt.right == None):
            return
        self.ans.append(rt.val)
        if rt.left != None:
            self.dfsLeft(rt.left)
        else:
            self.dfsLeft(rt.right)
        
    def dfsLeaf(self, rt):
        if rt == None:
            return 
        if rt.left == None and rt.right == None:
            self.ans.append(rt.val)
            return
        self.dfsLeaf(rt.left)
        self.dfsLeaf(rt.right)
    
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
