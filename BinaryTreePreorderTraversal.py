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
   @return: Preorder in ArrayList which contains node values.
   """
   def preorderTraversal(self, root):
       # write your code here
       if not root:
           return []
       
       stack = [root]
       preorder = []

       while stack:
           node = stack.pop()
           preorder.append(node.val)
          
           if node.right:
               stack.append(node.right)
           if node.left:
               stack.append(node.left)
       return preorder
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.preorderTraversal(root)
    print(x)
    

