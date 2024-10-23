class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

def build_tree():
    node_1 = ParentTreeNode(1)
    node_2 = ParentTreeNode(2)
    node_3 = ParentTreeNode(3)
    node_4 = ParentTreeNode(4)

    node_1.left = node_2
    node_1.right = node_3
    node_1.parent = None

    node_2.left = node_4
    node_2.right = None
    node_2.parent = node_1

    node_3.left = None
    node_3.right = None
    node_3.parent = node_1

    node_4.left = None
    node_4.right = None
    node_4.parent = node_2

    return node_1

def binaryTreePathSum3(root, target):
        # Write your code here
        results = []
        dfs(root, target, results)
        return results

def dfs(root, target, results):
    if root is None:
        return
    
    path = []
    findSum(root, None, target, path, results)

    dfs(root.left, target, results)
    dfs(root.right, target, results)

def findSum(root, father, target, path, results):
    path.append(root.val)
    target -= root.val

    if target == 0:
        results.append(path[:])

    if root.parent not in [None, father]:
        findSum(root.parent, root, target, path, results)

    if root.left not in [None, father]:
        findSum(root.left, root, target, path, results)

    if root.right not in [None, father]:
        findSum(root.right, root, target, path, results)

    path.pop()

if __name__ == '__main__':
    root = build_tree()
    target = 3
    x = binaryTreePathSum3(root, target)
    print(x) 
    
   

