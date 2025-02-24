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
"""
# Method 1 Recursion Version Answer
class Solution:
   
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
"""
# Method 2 Non Recursion Version
class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        #如果root是空，就找到插node的地方
        if root is None:
            return node
        
        #先用一个curt指向root    
        curt = root

        #比较curt和要插的node是否相等，如果不等，比较大小
        while curt != node:
            #如果要插的node的值小于curt值，很有可能可以插到root的左孩子
            if node.val < curt.val:
                #这里要判断curt是不是已经有了左孩子，如果没有左孩子，直接连
                if curt.left is None:
                    curt.left = node
                #当curt有左孩子的时候，curt指向它的左孩子， 在进行比较
                curt = curt.left
            else:
                #如果node的值大于curt值，很可能可以插到curt的右孩子位置
                #当然要先检查，curt的右孩子为空，才行，否则，走向curt.right在比较
                if curt.right is None:
                    curt.right = node
                curt = curt.right
        return root

if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    node = TreeNode(6)
    x = ll.insertNode(root, node)
    print(x)
    


