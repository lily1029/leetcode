
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
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        # this is Iterator Version:
        if not root:
            return []
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        
        inorder = []
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                inorder.append(stack[-1].val)
        return inorder
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.inorderTraversal(root)
    print(x)