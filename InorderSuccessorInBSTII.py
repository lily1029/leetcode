class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None

def build_tree():
    node_1 = ParentTreeNode(2)
    node_2 = ParentTreeNode(1)
    node_3 = ParentTreeNode(3)
   
    node_1.left = node_2
    node_1.right = node_3
    node_1.parent = None

    node_2.left = None
    node_2.right = None
    node_2.parent = node_1

    node_3.left = None
    node_3.right = None
    node_3.parent = node_1

    return node_1


class Solution:
    """
    @param node: random node in binary search tree
    @return: the inorder successor of current node
    """
    def inorder_successor(self, node) :
        #因为是BST,我们要充分利用这点，所以如果它有右孩子，首先考虑会是它的successor
        #如果右孩子存在，node指向右孩子
        if node.right:
            node = node.right
            #此时如果右孩子还有下层的左孩子节点，在走向左，一直走到叶子节点，
            while node.left:
                node = node.left
            #最后返回这个点，一定是它的下一个successor
            return node

        #这里处理一个节点的下一个successor是none的情况
        while node.parent and node == node.parent.right:
            node = node.parent
        #最后返回none的情况
        return node.parent

if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    p = root.right
    x = ll.inorder_successor(p)
    print(x)







