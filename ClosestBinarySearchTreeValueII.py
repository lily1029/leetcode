class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(3)
    node_2 = TreeNode(1)
    node_3 = TreeNode(4)
    node_4 = TreeNode(2)
   
    node_1.left = node_2
    node_1.right = node_3

    node_2.right = node_4

    return node_1

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        if root is None or k == 0:
            return []
            
        lower_stack = self.get_stack(root, target)
        # let upper_stack equals to lower_stack
        upper_stack = list(lower_stack)

        # now the stack top has the smallest element in
        # the left subtree of this BST, if target > stack top value ,
        # move to move_upper, otherwise to lower_stack
        if lower_stack[-1].val < target:
            self.move_upper(upper_stack)
        else:
            self.move_lower(lower_stack)
        
        result = []
        for i in range(k):
            if self.is_lower_closer(lower_stack, upper_stack, target):
                result.append(lower_stack[-1].val)
                self.move_lower(lower_stack)
            else:
                result.append(upper_stack[-1].val)
                self.move_upper(upper_stack)
                
        return result
    
    # this method is to help lower_stack and return
    # stack from root to all the way down to left     
    def get_stack(self, root, target):
        stack = []
        while root:
            stack.append(root)
            if target < root.val:
                root = root.left
            else:
                root = root.right
                
        return stack
        
    def move_upper(self, stack):
        if stack[-1].right:
            node = stack[-1].right
            while node:
                stack.append(node)
                node = node.left
        else:
            node = stack.pop()
            while stack and stack[-1].right == node:
                node = stack.pop()
                
    def move_lower(self, stack):
        if stack[-1].left:
            node = stack[-1].left
            while node:
                stack.append(node)
                node = node.right
        else:
            node = stack.pop()
            while stack and stack[-1].left == node:
                node = stack.pop()
                
    def is_lower_closer(self, lower_stack, upper_stack, target):
        if not lower_stack:
            return False
            
        if not upper_stack:
            return True
            
        return target - lower_stack[-1].val < upper_stack[-1].val - target
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    target = 0.275000
    k = 2
    x = ll.closestKValues(root, target, k)
    print(x)
    

