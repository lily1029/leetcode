class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.children = []  # children is a list of MultiTreeNode objects

    def add_child(self, child_node):
        self.children.append(child_node)


class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    #从根结点开始dfs，每次搜相邻的相差1的结点，跟新即可
    def longestConsecutive3(self, root):
        # Write your code here
        #调用helper()函数， max_len 是一个global variable 看哪条path最长
        max_len, _, _, = self.helper(root)

        #并返回这个最长值
        return max_len
    
    def helper(self, root):

        #当root为空时，最长， 上，下 都初始值为0
        if root is None:
            return 0, 0, 0

        max_len, up, down = 0, 0, 0

        #for 循环root下的每一个孩子
        for child in root.children:

            #递归调用这个孩子
            result = self.helper(child)

            #更新global 值
            max_len = max(max_len, result[0])

            #这里是看从child + 1 往上走，看等于root 不， 如果等于，一条合法path
            if child.val + 1 == root.val: #对于root是down值 变大
                down = max(down, result[1] + 1) #这里对于child是up + 1

            if child.val - 1 == root.val:#对于root是up增加1
                up = max(up, result[2] + 1)#对于child 是down + 1

        #这里更新global max_len, 因为 down + 1(root)+ up 是新的合法path
        max_len = max(down + 1 + up, max_len)

        #返回global, down, up 值
        return max_len, down, up
if __name__ == '__main__':
    root = MultiTreeNode(5)
    child1 = MultiTreeNode(6)
    child2 = MultiTreeNode(4)
    root.add_child(child1)
    root.add_child(child2)

    child1.add_child(MultiTreeNode(7))
    child1.add_child(MultiTreeNode(5))
    child1.add_child(MultiTreeNode(8))

    child2.add_child(MultiTreeNode(3))
    child2.add_child(MultiTreeNode(5))
    child2.add_child(MultiTreeNode(31))

    ll= Solution()
    x = ll.longestConsecutive3(root)
    print(x)




