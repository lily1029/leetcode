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
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        #set predecessor as None at beginning
        pred = None
        
        #这里要充分利用BST的性质，所以p点和root值进行比较
        #因为要找predecessor，我们要找p点的前一个点，所以，
        #如果root值大于等于p点值，我们应该往root的左子树走
        #当root不为空时
        while root:

            #如果root.val大于p.val，不需要往右走，因为predecessor
            #在前，所以，往左走
            if root.val >= p.val:
                root = root.left 
            else:
                #此情况是root小于p.val的情况
                #这里找到了离p点最近的predecessor，如果pred为空，
                #先把pred设置为root值
                #但是这个root很有可能还有右孩子，所以要继续往右走，
                #直到找到最右边的值是它的pred
                if pred == None or root.val > pred.val:
                    pred = root
                root = root.right
        return pred
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    p = root
    x = ll.inorderPredecessor(root, p)
    print(x.val)

