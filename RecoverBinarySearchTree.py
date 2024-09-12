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
        
        #这里call 中序遍历inOrder(root)
        self.inOrder(root)
        
        #中序遍历完后，并且找到了first和second，进行交换
        #当最后找到了first和second后，交换
        if self.first != None:
            self.first.val, self.second.val = self.second.val, self.first.val 
        
        return root 
       
      
    #这里中序遍历（左中右）   
    def inOrder(self, root):
        if not root:
            return 
        self.inOrder(root.left)
        if self.pre != None:
            #在中序遍历的过程中，如果找到pre>root时，说明我们
            #找到了第一个错误的node 
            if self.first == None and self.pre.val > root.val:
                #第一个等于pre这里找到第一个
                self.first = self.pre
                #第二个等于root 
                self.second = root
            elif self.first != None and self.pre.val > root.val:
                #当第一个以找到，如果pre>val,那么第二个也找到
                self.second = root #second 等于root 
        #最初要先把pre设置成root
        self.pre = root 
        self.inOrder(root.right)
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.bstSwappedNode(root)
    print(x.val)