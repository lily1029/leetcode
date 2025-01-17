class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(10)
    node_2 = TreeNode(1)
    node_3 = TreeNode(11)
    node_4 = TreeNode(6)
    node_5 = TreeNode(12)
   
    node_1.left = node_2
    node_1.right = node_3
    
    node_2.right = node_4
    node_3.right = node_5

    return node_1


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        dummy = TreeNode(0)
        dummy.right = root
        self.stack = [dummy]
        self._next()

    """
    @return: True if there has next node, or false
    """
    #此函数判断true if there has next node in stack, or false
    def hasNext(self):
        return bool(self.stack)

    """
    @return: return next node
    """
    #此函数return next inorder node
    #此函数return the next smallest element in BST
    def _next(self):
        #这里弹出栈顶element, 栈顶弹出的就是最小的节点，我们把
        #它存在next_node variable里，因为向左子树压完所有的点入栈后
        #要返回之前栈点弹出的最小的点
        node = self.stack.pop()
        #next_node里存栈顶弹出的最小的节点
        next_node = node
        #这里和上一道题一样，走完全部左子树的节点，并压栈这一路的节点
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        #返回最小值，其实是按BST inorder 的下一个值，值的顺序是非递减
        return next_node
if __name__ == '__main__':
    root = build_tree()
    ll = BSTIterator(root)
    y = ll._next()
    print(str(y.val))
    x = ll.hasNext()
    print(x)
    



