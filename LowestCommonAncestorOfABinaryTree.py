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
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the lowest common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # 如果 A 和 B 都在，return  LCA
        # 如果只有 A 在，return A
        # 如果只有 B 在，return B
        # 如果 A, B 都不在，return None
        if root is None:
            return None
        
        if root.val == A or root.val == B:
            return root
        
        left_result = self.lowestCommonAncestor(root.left, A, B)
        right_result = self.lowestCommonAncestor(root.right, A, B)
        
        # A 和 B 一边一个
        if left_result and right_result: 
            return root
        
        # 左子树有一个点或者左子树有LCA
        if left_result:
            return left_result
        
        # 右子树有一个点或者右子树有LCA
        if right_result:
            return right_result
        
        # 左右子树啥都没有
        return None
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.lowestCommonAncestor(root, 3, 5)
    print(x.val)