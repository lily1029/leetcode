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
        
        #因为此树是BST，所以所有节点值应该是递增的，这里pre的值代表前一个节点
        #当pre的值大于下一个节点时，我们就找到了第一个出错的点，赋值给first,
        #然后继续找下一个， 最开始全部设置为none
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
        #corner case
        if not root:
            return 
        
        #中序遍历中的，遍历root的左子树
        self.inOrder(root.left)

        if self.pre != None:
            #在中序遍历的过程中，如果找到pre>root时，说明我们
            #找到了第一个错误的node 
            if self.first == None and self.pre.val > root.val:
                #第一个等于pre, 这里找到第一个first
                self.first = self.pre
                #第二个等于root
                #上面pre >root,所以第二个second 很可能是当前的root,所以赋值second为root 
                self.second = root
            elif self.first != None and self.pre.val > root.val:
                #当第一个以找到，如果pre>val,那么第二个也找到
                #second 等于root
                self.second = root 

        #这里是中序遍历中的中，也就是root的值，把pre的值赋值为root的值，以便下一次进行比较 
        self.pre = root 

        #中序遍历中的左中右的右边遍历
        self.inOrder(root.right)
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.bstSwappedNode(root)
    print(x.val)




