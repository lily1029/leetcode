class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(3)
    node_3 = TreeNode(2)
    node_4 = TreeNode(4)
    
   
    node_1.right = node_2

    node_2.left = node_3
    node_2.right = node_4


    return node_1


class Solution:
   
    #此题做法用divide and conquer， 从root开始，算出左子树的有效consecutive sequ path长度
    #算出右子树的consecutive sequence path 长度，然后选出左右子树中的最大（长）的。因为这2条
    #路径很有可能+ root也是一条更长合法的路径，这里用到一个global variable len to track the 
    #longest consecutive sequence path

    def longestConsecutive(self, root):

        #函数入口， root, root的parent值， sequence长度为0最初
        return self.helper(root, None, 0)
    
    #定义函数， root, root的parent值， sequence长度
    def helper(self, root, parent, len):

        #当root 为空时，返回现有这条路径上已有的有效consecutive sequence path
        if root is None:
            return len

        #这里判断是否符合consecutive sequence,如果父亲节点不为空，
        #并且孩子节点比父亲节点大一，是一个 合法的consecutive sequence
        if parent != None and root.val == parent.val + 1:
            #len 长度加一
            len += 1
        else:
            #否则一个点，len 只是1
            len = 1
        
        #以root为根的 左子树的consecutive sequence 长度 divide part 算左子树path值
        left_path = self.helper(root.left, root, len)

        #以root为根的右子树的consecutive sequence 长度， divide part 算右子树 path值
        right_path = self.helper(root.right, root, len)

        #以root为根的选左右子树中最大的consecutive sequence,
        #并和global len 比较，选最长的 conquer part
        return max(len, max(left_path, right_path ))
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.longestConsecutive(root)
    print(x)