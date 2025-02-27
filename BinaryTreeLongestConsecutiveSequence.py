class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def build_tree():
    node_1 = TreeNode(1)
    node_2 = TreeNode(3)
    node_3 = TreeNode(2)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
   
    node_1.right = node_2

    node_2.left = node_3
    node_2.right = node_4

    node_4.right = node_5

    return node_1


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    #此题做法用divide and conquer
    
    def longestConsecutive(self, root):
        #函数入口， root, root的parent值， sequence长度
        return self.helper(root, None, 0)
    
    #定义函数， root, root的parent值， sequence长度
    def helper(self, root, parent, len):

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
        
        #以root为根的 左子树的consecutive sequence 长度
        left_path = self.helper(root.left, root, len)

        #以root为根的右子树的consecutive sequence 长度
        right_path = self.helper(root.right, root, len)

        #以root为根的选左右子树中最大的consecutive sequence,
        #并和global len 比较，选最长的
        return max(len, max(left_path, right_path ))
if __name__ == '__main__':
    root = build_tree()
    ll = Solution()
    x = ll.longestConsecutive(root)
    print(x)