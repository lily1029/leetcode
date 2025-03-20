class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
   
    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    return node_1

class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    对于叶子结点将其高度置为0。 对于任一非叶子节点，其高度等于左右子树中高度的最大值加一
    """
    def __init__(self):
        #这里存放拨开每层放的叶子结点结果
        self.leaves = []
    
    def findLeaves(self, root):
        #这里调用tree_height()函数
        self.tree_height(root)
        
        #返回结果
        return self.leaves
    
    def tree_height(self, root):

        #root为None时，return -1
        if root == None:
            return -1 
        
        #调用左子树
        left_height = self.tree_height(root.left)
        #调用右子树
        right_height = self.tree_height(root.right)

        #上层节点的高度(这里选出这层左右子树高度最大值在加一，是上层的高度)
        height = 1 + max(left_height, right_height)

        #这里判断叶子节点在哪层
        if height >= len(self.leaves):
            #不同的层，新开一个list[] 
            self.leaves.append([])

        #这里保证同一层的叶子节点在同一个list里
        self.leaves[height].append(root.val)

        #返回当层的height,为上一层用
        return height

if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.findLeaves(root)
    print(x)

    


