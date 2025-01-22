class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(2)
    node_2 = TreeNode(1)
    node_3 = TreeNode(3)
   
    node_1.left = node_2
    node_1.right = node_3

    return node_1


class Solution:
    """
    此题的做法是我们对给定的BST进行中序遍历，一棵有效的BST的中序遍历是
    非递减（ascending order）,当我们中序遍历完后，我们从头到尾走一遍，如果
    任何node不是ascending order, 则此树就不是valid BST tree
    """
    def isValidBST(self, root):
        #这里存中序遍历完BST后的所有节点顺序
        self.res = []
        #对这个树进行中序遍历
        self.inorder(root)

        #go through中序遍历后的结果，看有没有违规的node
        for i in range(1, len(self.res)):
            #如果这里成立，说明it is not ascending order, return false
            if self.res[i] <= self.res[i - 1]:
                return False
        return True 
    

    #这里是递归版中序遍历
    def inorder(self, root):
        if not root:
            return 
        
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)

if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.isValidBST(root)
    print(x)


