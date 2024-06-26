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
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.left =node_6 

    return node_1
#前序遍历写法
# class Solution:
#     def count_nodes(self, root):
#         # write your code here
#         def pre_order(node):
#             if node is None:
#                 return 0

#             left_nodes = pre_order(node.left)
#             right_nodes = pre_order(node.right)
            
#             return left_nodes + right_nodes + 1
#         return pre_order(root)

class Solution:
    """
    @param root: root of complete binary tree
    @return: the number of nodes
    """
    def count_nodes(self, root: TreeNode) -> int:
        # write your code here
        if root is None:
            return 0 
        
        #get left of the tree height
        def lheight_tree(node):
            if not node:
                return 0 
            left_Treeheight = lheight_tree(node.left)
            return 1 + left_Treeheight
        
        #get left of the tree height
        def rheight_tree(node):
            if not node:
                return 0
            right_Treeheight = rheight_tree(node.right)
            return 1 + right_Treeheight
        
        l = lheight_tree(root)

        r = rheight_tree(root)

        #如果左边tree height 大于右边tree height, 就recursively算出左子树的nodes number + 右子树nodes number + 1(root number)
        if l > r:
            return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)
        else:
            return (2**l) - 1 #这里如果左右子树高度一样，就用perfect complete binary tree 公式算所有nodes number (2^l) - 1  l is tree height

    
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.count_nodes(root)
    print(x)
