class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(4)
    node_2 = TreeNode(3)
    node_3 = TreeNode(7)
    node_4 = TreeNode(5)
    node_5 = TreeNode(6)
   
    node_1.left = node_2
    node_1.right = node_3

    node_3.left = node_4
    node_3.right = node_5

    return node_1

class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    #这道题存在有些点是Non的情况
    def lowestCommonAncestor3(self, root, A, B):
        #所以这里我们判断一下
        a, b, lca = self.helper(root, A, B)
        
        #如果左子树的结果在，并且右子树的结果在，这是返回lca,否则返回none
        if a and b:
            return lca
        else:
            return None 
    
    #divide conquer algorithm
    def helper(self, root, A, B):
        #当根节点为空时
        if not root:
            #返回左子A值为false, 右子树B节点为false, 根节点为none 
            return False, False, None

        #divide
        #这里判断左子树是否有a 的值，左子树是否有b的值， 左子树返回结果    
        left_a, left_b, left_node = self.helper(root.left, A, B)
        #这里判断右子树是否有a 的值，右子树是否有b的值， 右子树返回结果    
        right_a, right_b, right_node = self.helper(root.right, A, B)
        
        #这里返回左子树的值,并赋值给，a， 注意a是一个boolen 值，true, or fase
        #有A的值为true, 没有A为false 
        a = left_a or right_a or root == A
        #这里返回右子树的值给b
        b = left_b or right_b or root == B 
        
        #conquer part
        #如果A, B在root上，则返回root
        if root == A or root == B:
            return a, b, root 
        
        #如果左子树有值而且右子树有值，返回共同的根节点
        if left_node and right_node:
            return a, b, root
        #如果只有左子树有值，返回左子树值， 这里的a, b 是判断true, fase，是否有A, B值
        if left_node:
            return a, b, left_node
        #如果只有右子树有值，返回右子树值， 这里的a, b 是判断true, fase，是否有A, B值
        if right_node:
            return a, b, right_node
        #当 a, b 都为false, 都没值时，返回 none 
        return a, b, None
if __name__ == '__main__':
    root = build_tree()
    node_3 = root.left
    node_5 = root.right.left  
    node_6 = root.right.right   
    node_7 = root.right
    node_8 = None
    ll = Solution()
    x = ll.lowestCommonAncestor3(root, node_3, node_5)
    print(x.val)


