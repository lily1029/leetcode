class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(2)
    node_2 = TreeNode(1)
    node_3 = TreeNode(4)
    node_4 = TreeNode(3)
   
    node_1.left = node_2
    node_1.right = node_3
    
    node_3.left = node_4

    return node_1

class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # 当root为空时，就是找到该插这个node的地方，所以返回node
        if not root:
            return node 
        
        #充分利用bst性质，root的值先和插入的node进行比较
        #如果root的值大于node的值，走向root的左子树，调用recursion向左
        if root.val > node.val:
            root.left = self.insertNode(root.left, node)
        else:
            #否则走向root的右子树，继续recursion向右
            root.right = self.insertNode(root.right, node)
        
        return root
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    node = TreeNode(6)
    x = ll.insertNode(root, node)
    print(x)
    

