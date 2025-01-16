class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(3)
    node_2 = TreeNode(5)
    node_3 = TreeNode(1)
    node_4 = TreeNode(6)
    node_5 = TreeNode(2)
    node_6 = TreeNode(0)
    node_7 = TreeNode(8)
    node_8 = TreeNode(7)
    node_9 = TreeNode(4)
   
    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    node_5.left = node_8
    node_5.right = node_9

    return node_1

class Solution:
    """
    @param root: The root node of a binary tree.
    @param nodes: An array of objects of class TreeNode.
    @return: The lowest common ancestor of nodes.
    """
    def lowest_common_ancestor(self, root, nodes):
        # --- write your code here ---
        def dfs(root):
            if root is None or root.val in s:
                return root
            left, right = dfs(root.left), dfs(root.right)
            if left and right:
                return root
            return left or right

        s = {node.val for node in nodes}
        return dfs(root)
if __name__ == '__main__':
    root = build_tree()
    node7 = root.left.right.left
    node6 = root.left.left
    node2 = root.left.right 
    node4 = root.left.right.right
    ll = Solution()
    nodes = [node7, node6, node2, node4]
    x = ll.lowest_common_ancestor(root, nodes)
    print(x.val)


