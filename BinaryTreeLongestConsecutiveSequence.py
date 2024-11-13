class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(3)
    node_3 = TreeNode(2)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
   
    node_1.right = node_2

    node_2.left = node_3
    node_2.right = node_4

    node_4.right = node_5

    return node_1


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive(self, root):
        # Write your code here
        return self.helper(root, None, 0)
    
    def helper(self, root, parent, len):
        if root is None:
            return len

        if parent != None and root.val == parent.val + 1:
            len += 1
        else:
            len = 1
        return max(len, max(self.helper(root.left, root, len), self.helper(root.right, root, len)))
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.longestConsecutive(root)
    print(x)