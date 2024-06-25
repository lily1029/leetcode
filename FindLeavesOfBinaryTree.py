class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
   
    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    return node_1

class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def __init__(self):
        self.leaves = []
    
    def findLeaves(self, root):
        # write your code here
        self.tree_height(root)
        
        return self.leaves
    
    def tree_height(self, root):
        if root == None:
            return -1 
        left_height = self.tree_height(root.left)
        right_height = self.tree_height(root.right)
        height = 1 + max(left_height, right_height)
        if height >= len(self.leaves):
            self.leaves.append([])
        self.leaves[height].append(root.val)
        return height

if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.findLeaves(root)
    print(x)