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

def traverse_tree(root):
    if not root:
        return None
    print(root.val, end = ' ')
    traverse_tree(root.left)
    traverse_tree(root.right)

def levelOrder(root):
        # write your code here
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

if __name__ == '__main__':
    root = build_tree()
    #traverse_tree(root)

    x = levelOrder(root)
    print(x)

