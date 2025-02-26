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
    """
    @param root: the root of the tree
    @return: the total sum of all root-to-leaf numbers
    """
    def sumNumbers(self, root):
        # write your code here
        return self.dfs(root, 0);

    def dfs(self, root, prev):
        #if root is none, we return 0
        if(root == None) :
            return 0;

        #如果当前节点不是叶子节点，则计算其子节点对应的数字，然后对子节点递归遍历。
        sum = root.val + prev * 10;

        #如果遇到叶子节点，
        #则将叶子节点对应的数字加到数字之和。
        if(root.left == None and root.right == None) :
            return sum;

        #深度优先搜索是很直观的做法。从根节点开始，遍历每个节点，
        #如果当前节点不是叶子节点，则计算其子节点对应的数字，然后对子节点递归遍历。
        return self.dfs(root.left, sum) + self.dfs(root.right, sum);

if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.sumNumbers(root)

    print(x)
