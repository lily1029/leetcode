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
   @return: Postorder in ArrayList which contains node values.
   """
   def postorderTraversal(self, root: TreeNode):
       stack = []
       output = []
       if not root:
           return output
       stack.append(root)
       while stack:
           node = stack.pop()
           output.insert(0, node.val)
           if node.left:
               stack.append(node.left)
           if node.right:
               stack.append(node.right)
       return output

if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.postorderTraversal(root)
    print(x)
    