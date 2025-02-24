class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(6)
    node_2 = TreeNode(2)
    node_3 = TreeNode(8)
    node_4 = TreeNode(0)
    node_5 = TreeNode(4)
    node_6 = TreeNode(7)
    node_7 = TreeNode(9)
    node_8 = TreeNode(3)
    node_9 = TreeNode(5)
   
    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    node_5.left = node_8
    node_5.right= node_9

    return node_1


class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
    	# root 等于 p 或 q, 直接返回root
        if root == p or root == q:
            return root

        # p, q 的值都小于root的值， 那就继续到左子树去找
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # p, q 的值都大于root的值， 那就去右子树里找lca
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # p, q 分别在左右子树，那么root即为结果
        return root
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    p = root.left
    q = root.right
    x = ll.lowestCommonAncestor(root, p, q)

    print(x.val)


