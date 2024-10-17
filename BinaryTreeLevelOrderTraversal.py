from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)

    node_1.left = node_2
    node_1.right = node_3

    return node_1

# def traverse_tree(root):
#     if not root:
#         return None
#     print(root.val, end = ' ')
#     traverse_tree(root.left)
#     traverse_tree(root.right)

def levelOrder(root):
        #这道题的主要思想是用一个queue,利用它的先进先出
        #将二叉树每层的节点放入queue中，遍历queue直到遍历完
        #corner case
        if not root:
            return []
        #initize a queue
        queue = deque([root])
        result = []

        #loop through the queue
        while queue:
            #对每一层放入一个[]里，来区分不同层
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #将所有层的结果放入result中
            result.append(level)
        return result

if __name__ == '__main__':
    root = build_tree()
    #traverse_tree(root)

    x = levelOrder(root)
    print(x)

