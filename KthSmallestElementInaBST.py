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
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # use binary tree iterator
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        
        #look for kth smallest, we pop出k个节点，
        #剩下在栈顶的节点就是第kth smallest element
        #因为虽然是kth，因为index start from 0    
        for i in range(k):
            # pop out the 栈顶元素
            node = stack.pop()

            # 查看pop出的元素是否有右子树，如果有
            # 更新node, 并且把左子树全部走完
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

            # if stack is empty, return None
            if not stack:
                return None
        
        #return 栈顶元素,即kth smallest element       
        return stack[-1].val

if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    k = 2
    x = ll.kthSmallest(root, k)
    print(x)


