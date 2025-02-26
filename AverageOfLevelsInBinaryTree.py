class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    node_1 = TreeNode(3)
    node_2 = TreeNode(9)
    node_3 = TreeNode(20)
    node_4 =  TreeNode(15)
    node_5 = TreeNode(7)
    
    node_1.left = node_2
    node_1.right = node_3

    node_3.left = node_4
    node_3.right = node_5

    return node_1

class Solution:
    """
    @param root: the binary tree of the  root
    @return: return a list of double
    """
    #这道题的做法就是对这颗二叉树进行bsf, 先把root放入一个queue里
    #当queue不为空时，循环这个queue,把binary tree的 每层节点放入queue中，
    #然后算每层的average = sum(几个点的值)/几个节点

    def averageOfLevels(self, root):
        # 放最终结果
        res = []

        #初始一个queue,并把root放入进来 
        queue = [root]

        #当queue不为空时，
        while queue:
            #存每层的节点的variable
            temp = []
            #按queue的长度进行for 循环
            for i in range(len(queue)):
                #弹出queue中第一个节点，并赋值给node
                node = queue.pop(0)
                #将node值放入到temp中，这样binary tree中每一层节点都在一起
                temp.append(node.val)
                
                #并且查看这个node是不是有左右孩子，如果有，放入queue中
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            #这里算每一层的average
            if temp:
                res.append(sum(temp)/len(temp))
        return res
    
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()

    x = ll.averageOfLevels(root)
    print(x) 
    
    
