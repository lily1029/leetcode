class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)

    node_1.left = node_2
    node_1.right = node_3

    return node_1

class Solution:
    def sum_numbers(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, prevTotal: int) -> int:
            #if root is none, we return 0
            if not root:
                return 0
            #如果当前节点不是叶子节点，则计算其子节点对应的数字，然后对子节点递归遍历。
            total = prevTotal * 10 + root.val
            #如果遇到叶子节点，
            #则将叶子节点对应的数字加到数字之和。
            if not root.left and not root.right:
                return total
            else:
                #深度优先搜索是很直观的做法。从根节点开始，遍历每个节点，
                #如果当前节点不是叶子节点，则计算其子节点对应的数字，然后对子节点递归遍历。
                return dfs(root.left, total) + dfs(root.right, total)

        return dfs(root, 0)

if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.sum_numbers(root)

    print(x)
