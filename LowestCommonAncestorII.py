class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.parent = None, None, None

def build_tree():
    node_1 = TreeNode(4)
    node_2 = TreeNode(3)
    node_3 = TreeNode(7)
    node_4 = TreeNode(5)
    node_5 = TreeNode(6)
   
    node_1.left = node_2
    node_1.right = node_3
    node_2.parent = node_1
    node_3.parent = node_1

    node_3.left = node_4
    node_3.right = node_5
    node_4.parent = node_3
    node_5.parent = node_3

    return node_1

class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        parentSet = set()
        
        cur = A 
        while cur:
            parentSet.add(cur)
            cur = cur.parent
        
        cur = B 
        while cur:
            if cur in parentSet:
                return cur
            cur = cur.parent
        return None
if __name__ == '__main__':
    root = build_tree()
    node_3 = root.left
    node_5 = root.right.left    
    ll = Solution()
    x = ll.lowestCommonAncestorII(root, node_3, node_5)
    print(x.val)