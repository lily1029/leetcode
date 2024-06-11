class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    
    node_1.left = node_2
    node_1.right = '#'

    node_2.left = '#'
    node_2.right = '#'

    return node_1

def serialize(root):
        # write your code here
        if not root:
            return ['#']
        
        q = [root]
        ans = []

        while q:
            temp = q.pop(0)
            if not temp:
                ans.append('#')
            else:
                ans.append(str(temp))
                q.append(str(temp.left))
                q.append(str(temp.right))
        return ans 

if __name__ == '__main__':
    root = build_tree()
    x = serialize(root)
    print(x)
    
