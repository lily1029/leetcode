class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(4)
    node_2 = TreeNode(5)
    node_3 = TreeNode(2)
    node_4 = TreeNode(1)
    node_5 = TreeNode(3)
   
    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    return node_1
class Solution:
    """
    @param root: the given tree
    @return: the tree after swapping
    """
    def bstSwappedNode(self, root):
        #here is corner case,if root is None, return None 
        if not root:
            return None 
        
        self.pre = None 
        self.first = None 
        self.second = None 
        
        self.inOrder(root)
        
        if self.first != None:
            self.first.val, self.second.val = self.second.val, self.first.val 
        
        return root 
       
      
    #这里中序遍历（左中右）   
    def inOrder(self, root):
        if not root:
            return 
        self.inOrder(root.left)
        if self.pre != None:
            if self.first == None and self.pre.val > root.val:
                self.first = self.pre
                self.second = root
            elif self.first != None and self.pre.val > root.val:
                self.second = root
        self.pre = root 
        self.inOrder(root.right)
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.bstSwappedNode(root)
    print(x.val)