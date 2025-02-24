class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(-5)
    node_3 = TreeNode(11)
    node_4 = TreeNode(1)
    node_5 = TreeNode(2)
    node_6 = TreeNode(4)
    node_7 = TreeNode(-2)
   
    node_1.left = node_2
    node_1.right = node_3
    
    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    return node_1

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    #为了找到这颗树的subtree with maximum average, 我们可以利用
    #divide and conquer method, 每棵树，得到它的左子树的值和节点个数
    #算平均值，然后在得到它的右子树的值和节点个数，算平均值， 然后算这棵树
    #总的值和节点数算平均值，进行比较，这里设置一个golobal valiable
    #to track the maximum average 
    # global variables to find max average, and max node
    average, node = 0, None

    def find_subtree2(self, root: TreeNode) -> TreeNode:
        # 这里调用 divide and conquer method
        self.helper(root)
        #这里返回最大的maximum average 的root
        return self.node

    #divide and conquer method
    def helper(self, root):
        #当一棵树的root为空时，它的子树值为0，节点个数为0
        if root is None:
            return 0, 0
        
        # divide left and right subtree
        #算左子树的值和节点个数是left_size
        left_sum, left_size = self.helper(root.left)
        #算右子树的值和节点个数
        right_sum, right_size = self.helper(root.right)
        
        # conquer and configure out sum of this subtree 
        #算这棵树的值和节点个数（conquer part）
        sum = left_sum + right_sum + root.val
        size = left_size + right_size + 1
        
        # update global variables
        if self.node is None or sum / size > self.average:
            self.node = root
            self.average = sum  / size

        #返回数的值和节点个数
        return sum, size
    
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    
    x = ll.find_subtree2(root)
    print(x)
    


