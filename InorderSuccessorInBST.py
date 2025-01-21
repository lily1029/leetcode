class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(2)
    node_2 = TreeNode(1)
    node_3 = TreeNode(3)
   
    node_1.left = node_2
    node_1.right = node_3

    return node_1


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        #首先我们先把successor设置为None
        successor = None
        #对root不为空进行循环
        while root:
            #充分利用binary search的特性，如果root.val > p.val,
            #root有可能成为它的successor,如果p这个点没有右孩子,因为如果
            #p这个点有右孩子，p点的直接successor为p点的右孩子
            if root.val > p.val:
                successor = root
                #因为root.val >p.val，这个点很有可能有它的右孩子，
                #所以第二步是，root走向它的左子树进行彻底查找 
                root = root.left
            else:
                #在递归的几次中，最终我们们会找到p点的那个右孩子，
                #而且此时它变成了root,然后在递归下一层时，
			    #因为root.val > p.val
                #所以successor = root, root也最终会指向空，而被返回终止
                root = root.right
         
        return successor

if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    p = TreeNode(1)
    x = ll.inorderSuccessor(root, p)
    print(x.val)


