class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(20)
    node_2 = TreeNode(8)
    node_3 = TreeNode(22)
    node_4 = TreeNode(4)
    node_5 = TreeNode(12)
   
    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    return node_1


class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def search_range(self, root: TreeNode, k1: int, k2: int):
        # write your code here
        result = []
        self.travel(root, k1, k2, result)
        return result
        
    
    def travel(self, root, k1, k2, result):
        if not root:
            return 
        
        #先对root的值和左边界k1的值进行比较，如果root的值大于左边界，责继续去root的左子树找值
        if root.val > k1:
            #递归调用左子树
            self.travel(root.left, k1, k2, result)
        #这里找到了节点的值在左右边界之中的，所以可以放到result中
        if k1 <= root.val and root.val <= k2:
            result.append(root.val)
        #此时还要继续看看这个root的右子树的孩子是不是也在两个边界之间，符合题目要求
        if root.val < k2:
            #递归调用右子树
            self.travel(root.right, k1, k2, result)

      
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    k1 = 10
    k2 = 22
    x = ll.search_range(root, k1, k2)
    print(x)


