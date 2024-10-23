class Solution:
    """
    @param nums: a list of integers
    @return: return an integer
    """

    def pathSum(self, nums):
        # Find the number of nodes and initialize size of the grid
        n = len(nums)
        siz = 1
        
        # Determine the maximum depth of the tree and initialize the result
        #self.ans是最后的结果
        self.ans = 0
        #因为nums里的数字是ascending, 所以可以通过最后一个数//100算出树的深度
        #这里树的深度其实是矩阵的行数，如果一个三位数想得到百位数，整出100得百位数字
        # 221 // 100 = 2， 树的深度为2，放入的矩阵，矩阵的行数为2
        #self.mx 是矩阵的行数，这个例子，行数为2
        self.mx = nums[n - 1] // 100
        
        # Calculate the size of the grid based on the maximum depth
        #算出列数根据行数多少，这里self.mx是行数为2，算出列数size至少为2
        #这里self.mx行数为2，n=3,有3个nodes的树，所以，列数至少为 2
        for i in range(self.mx - 1):
            siz *= 2
        
        # Initialize a grid with value -1，这里创建一个矩阵g
        g = []
        #这里for循环行数，行数是self.mx,对每一行加列叫row
        for i in range(self.mx):
            row = []
            #然后for循环列的数量，好放值，最开始的初始值都为-1
            for j in range(siz):
                #每一次循环到一列，就放一个初始值-1
                row.append(-1)
            #将所创的行列放入g矩阵中
            g.append(row)
        
        # Fill the grid with values from nums
        #这里for循环输入数组，算出每个数在矩阵中的行列位置
        for i in range(n):
            # Extract depth and position
            #算行位置row position
            dep = nums[i] // 100
            #算列position
            pos = nums[i] // 10 % 10
            
            # Place the value in the grid
            #因为grid是从g[0][0]开始，所以要减一
            #想得到一个数的最后一位 数字%10 e.g nums[i]%10
            g[dep - 1][pos - 1] = nums[i] % 10
        
        # Start DFS to calculate the path sums in the grid
        self.dfs(g, 0, 0, 0)
        
        # Return the final answer
        return self.ans

    # g means grid, d means dep也就是第几行，p means pos也就是第几列
    def dfs(self, g, d, p, sum):
        # Base case: If the current node is invalid, return
        # base case, 当走到叶子节点为-1， 结束，返回
        if g[d][p] == -1:
            return
        
        # Add the value of the current node to the sum
        sum += g[d][p]
        
        # Check if we are at the last depth or at a leaf node
        if d == self.mx - 1 or (g[d + 1][2 * p] == -1 and g[d + 1][2 * p + 1] == -1):
            # Add the sum of the path to the answer
            self.ans += sum
            return
        
        # Recursive DFS calls for left child nodes
        self.dfs(g, d + 1, 2 * p, sum)
        # Recursive DFS calls for right child nodes
        self.dfs(g, d + 1, 2 * p + 1, sum)

if __name__ == '__main__':
    ll = Solution()
    nums = [113, 215, 221]
    x = ll.pathSum(nums)
    print(x)
