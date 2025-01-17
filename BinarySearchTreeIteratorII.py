class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(7)
    node_2 = TreeNode(3)
    node_3 = TreeNode(15)
    node_4 = TreeNode(9)
    node_5 = TreeNode(20)
   
    node_1.left = node_2
    node_1.right = node_3

    node_3.left = node_4
    node_3.right = node_5
    
    return node_1


class BSTIterator:

    def __init__(self, root: TreeNode):
        #初始一个栈
        self.stack = []
        #调用help函数去进行非递归版本中序遍历BST
        self.help(root)
        
    #此函数相当于return下一个最小节点
    def next(self) -> int:
        """
        @return the next smallest number
        """
        #pop掉当前的栈顶节点，保存到n variable里，它已是当前最小节点
        n = self.stack.pop()
        #这里是弹出后的节点的下一节点，也是当前子节点(n)的右子节点，
        #刚刚比n大一点
        self.help(n.right)
        #这里返回n的节点值
        return n.val
        
        
    #此函数是看栈里有没有节点
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        #如果栈为空，返回false,否则返回true
        if self.stack == []:
            return False
        else:
            return True
    
    #这里的help函数，相当于直接把最初的root节点放入到栈里，然后从
    #root一直往左子树走，走到最左边的左子树的叶子节点
    def help(self, root):
        while root:
            self.stack.append(root)
            root = root.left
        
if __name__ == '__main__':
    root = build_tree()
    ll = BSTIterator(root)
    z = ll.next()
    print(z)
    y = ll.next()
    print(y)
    x = ll.hasNext()
    print(x)


