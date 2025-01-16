
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
    def flatten(self, root):
        # we use divide conquer algorithm
        self.helper(root)
    
    def helper(self, root):
        if not root:
            return None
        
        #divide part
        left_last = self.helper(root.left)
        right_last = self.helper(root.right)
        
        #connect the root to the two sub-trees
        #conquer part
        if left_last:
            left_last.right = root.right
            root.right = root.left 
            root.left = None
        
        if right_last:
            return right_last
        if left_last:
            return left_last
        return root

if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.flatten(root)
    print(x)

