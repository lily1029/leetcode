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

class Solution:
    # @param {ParentTreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum3(self, root, target):
        # Write your code here
        results = []
        #此题就是从root节点开始对每个节点进行三个方向的dfs, 三个方向是：这个节点的父亲节点，节点的左子树，节点的右子树， 
        #分别进行dfs直到找到符合答案的路径
        self.dfs(root, target, results)
        return results

    def dfs(self, root, target, results): 
        #dfs时传进去root, target, 和最后要知道的results
        #当root为空时，返回
        if root is None:
            return
        
        #定义一个variable 放路径
        path = [] 
        #这里用一个method叫findSum（）去找有效路径，传进去root节点，root节点的父亲节点，target,path, results. 
        self.findSum(root, None, target, path, results)
        #这里是对树中每个节点都当成一个新的（root)节点，进行dfs，传入的father节点初始值为None,然后在对father节点进行dfs
        #dfs root的左子树
        self.dfs(root.left, target, results)
        #dfs root的右子树
        self.dfs(root.right, target, results)

    def findSum(self, root, father, target, path, results):
        #现将root.val 放入到path中
        path.append(root.val)
        #这时候target 就变成 target - root.val
        target -= root.val 

        #这里判断下如果target=0, 我们找到了有效的path, 将path append到最终结果results里
        if target == 0: 
            results.append(path[:])

        #如果root.parent 不是空，root.parent不是它的parent才可以，如果root.parent的dfs已经完成，
        #就不可以在调用这个函数，因为在调用这个findsum函数是第一步就是对root.parent进行dfs,这里要避免2次dfs父亲节点
        if root.parent not in [None, father]: 
            self.findSum(root.parent, root, target, path, results)

        #如果root.left不是空，也不是父亲节点，就调用findsum函数，这里对root.left进行dfs,看它是否符合条件
        if root.left not in [None, father]: 
            self.findSum(root.left, root, target, path, results)

        #如果root.right不是空，不是父亲节点，就调用findsum函数，这里对root.right进行dfs,看它是否符合条件
        if root.right not in [None, father]: 
            self.findSum(root.right, root, target, path, results)

        #不满足以上条件，就back tracking,弹出最后一个
        path.pop()
    

if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    target = 3
    x = ll.binaryTreePathSum3(root, target)
    print(x) 
    
    
