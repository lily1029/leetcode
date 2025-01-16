class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
   
    node_1.left = node_2
    node_1.right = node_3

    return node_1


class Solution:
    """
    注意：此题为BST Iterator 模版（Binary Search Tree 非递归模版）
    """
    def inorderTraversal(self, root):
        # this is Iterator Version:
        if not root:
            return []
        
        #创建一个dummy node,它的右指针指向root,并将这个dummy node 
        #放入到stack里，此时stack的栈顶是dummy node
        #是iterator的当前位置
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        
        inorder = []
        #每次将iterator挪到下一个点，也就是调整stack使得栈顶到下一个点
        #当栈不为空时
        while stack:
            #弹出此点，并赋值给node variable
            node = stack.pop()
            #如果这个点有右子树
            if node.right:
                #指向右子树的点
                node = node.right
                #当这个点不为空时
                while node:
                    #先将这个点存入stack里
                    stack.append(node)
                    #在继续指向这个点的左子树，一直到空
                    #这里其实是将根节点压栈并一直压栈左子树的节点，一直到空
                    node = node.left
            
            #当stack里已经压栈了从root到它的左子树的所有节点完后，此时inorder
            #里接收栈顶元素，栈顶元素总放入到inorder list 里
            if stack:
                inorder.append(stack[-1].val)
        return inorder
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.inorderTraversal(root)
    print(x)