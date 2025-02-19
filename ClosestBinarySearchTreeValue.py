class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(3)
    node_2 = TreeNode(2)
    node_3 = TreeNode(4)
    node_4 = TreeNode(1)
   
    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4

    return node_1


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # 我们要找最接近的值，这个值必定在一个区间，
        #我们先把这个区间下限和上限都设为root，要充分利用bst的性质，
        #target 先和root的值进行比较
        upper = root
        lower = root 

        #当root不为空
        while root:
            #如果root的值小于target, root 可以做下限
            if root.val < target :
                lower = root 
                #然后走向root的右边，找大的值
                root = root.right
            #如果root的值大于target, root 的值可以做上限区间
            elif root.val > target:
                upper = root
                #然后向左走，找小一点的值
                root = root.left 
            else:
                #不在下区间，也不在上区间，必定就是root了
                return root.val 
        
        #最后比较target是离下限近还是上限近
        if abs(upper.val - target) <= abs(lower.val - target):
            return upper.val 
        return lower.val
    
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    target = 4.142857
    x = ll.closestValue(root, target)
    print(x)


   