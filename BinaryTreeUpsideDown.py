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
    

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4

    return node_1

class Solution:
    """
    @param root: the root of binary tree
    @return: new root
    """
    def upsideDownBinaryTree(self, root):
        #root为空，返回空
        if not root:
            return None 
        
        #root不为空，对root进行dfs()
        return self.dfs(root)
    
    #dfs时，把传进去的root点标为cur点
    def dfs(self, cur):
        #如果cur.left为空，返回cur
        if cur.left is None:
            return cur 
        
        #如果cur.left不为空，把cur.left设置为newroot
        newroot = TreeNode(cur.left)
        #并对newroot进行dfs()
        newroot = self.dfs(cur.left)
        
        #这里2是cur, cur.left就是4
        cur.left.right = cur 
        cur.left.left = cur.right
        #翻转完后，把2.left 和 2.right清空，
        cur.left = None 
        #以免形成环
        cur.right = None 
        
        return newroot
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.upsideDownBinaryTree(root)
    print(x)