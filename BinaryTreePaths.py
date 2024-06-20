
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(5)
   
    node_1.left = node_2
    node_1.right = node_3

    node_2.right = node_4

    return node_1


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        res = []
        def helper(root, cur):
            if not root:
                return 
            if not root.left and not root.right:
                res.append(cur + str(root.val))
            
            helper(root.left, cur + str(root.val) + "->")
            helper(root.right, cur + str(root.val) + "->")
        helper(root, "")
        return res
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.binaryTreePaths(root)
    print(x)