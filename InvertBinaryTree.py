class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
   
    node_1.left = node_2
    node_1.right = node_3

    return node_1


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invert_binary_tree(self, root: TreeNode):
        # write your code here
        if not root: 
            return None
        
        left_sub = self.invert_binary_tree(root.left)
        right_sub = self.invert_binary_tree(root.right)

        root.right = left_sub
        root.left = right_sub

        return root 

if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.invert_binary_tree(root)
    
    print(x)


