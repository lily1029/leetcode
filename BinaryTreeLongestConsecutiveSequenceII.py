class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(0)
    node_4 = TreeNode(3)
    
    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    

    return node_1


class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive2(self, root):
        #corner case
        if not root:
            return 0
        
        #global variable to track the longest sequence 
        self.length = 1
        #call dfs method
        self.search(root)
        #return the result
        return self.length
    
    def search(self, root):
        #当root为空时， 返回此root的最大上升长度up_length 为0
        #返回此root的 最大下降长度down_length 为0
        if not root:
            return [0, 0]
        
        #对每一个节点，它的 up_length 和 down_length 初始值为1
        up_length = 1
        down_length = 1

        #divide part to left subtree
        left = self.search(root.left)
        #divide part to right subtree 
        right = self.search(root.right)
        
        #在这里判断是不是可以找到一条合法路径
        if root.left:
            #加上头节点可以是合法路径，up_length + 1
            if root.left.val - 1 == root.val:
                up_length = max(up_length, left[0] + 1)
            #这里是可以找到一条合法的down_length 路径
            if root.left.val + 1 == root.val:
                down_length = max(down_length, left[1] + 1)
        
        #这里属于镜像操作，上面看root.left, 这里查看root.right做一样的操作
        if root.right:
            if root.right.val - 1 == root.val:
                up_length = max(up_length, right[0] + 1)
            if root.right.val + 1 == root.val:
                down_length = max(down_length, right[1] + 1)
        
        #更新全局变量最大值，包括加上root的值（up_length + down_length - 1)
        self.length = max(self.length, up_length + down_length - 1)
        
        #这里返回每个节点的最大上升长度up_length和最大下降长度down_length
        return [up_length, down_length]
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.longestConsecutive2(root)
    print(x)


