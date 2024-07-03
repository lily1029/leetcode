class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(5)
    node_5 = TreeNode(4)

    node_1.left = node_2
    node_1.right = node_3

    node_2.right = node_4

    node_3.right = node_5

    return node_1
from collections import deque
class Solution:
    """
    这道题用的方法是使用一个queue, 然后用level order traversal
    的方法，只是只收集每层的最后一个点，也就是满足这个条件i == n - 1:
    所得到的答案就是right tree
    """
    def rightSideView(self, root):
        # write your code here
        if not root:
            return []
        
        queue = deque([root])
        res = []

        while queue:
            #获取queue的size
            n = len(queue)
            #go through the queue, and popleft() one
            for i in range(n):
                node = queue.popleft()

                #满足此条件可以保存到right side tree nodes 
                if i == n - 1:
                    res.append(node.val)
                
                #接着扫描node左右节点的nodes
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.rightSideView(root)
    print(x)