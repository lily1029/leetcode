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

def serialize(root):
    # write your code here
    if not root:
        return ['#']
    
    q = [root]
    ans = []


    while q:
        node = q.pop(0)
        if not node:
            ans.append('#')
        else:
            ans.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
    return ans


def deserialize(data):
        # write your code here
        if data[0] == '#':
            return None
        root = TreeNode(int(data.pop(0)))
        q = [root]
        isLeft = True
        while data:
            ch = data.pop(0)
            if ch != '#':
                node = TreeNode(int(ch))
                q.append(node)
                if isLeft:
                    q[0].left = node
                else:
                    q[0].right = node
            if not isLeft:
                q.pop(0)
            isLeft = not isLeft
        return root

if __name__ == '__main__':
    root = build_tree()
    x = serialize(root)
    print("Serialized:", x)  # Should show a valid serialized tree representation
    
    y = deserialize(x)
    print("Deserialized Tree (level order):", y)




