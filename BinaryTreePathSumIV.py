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
        self.ans = 0
        #因为nums里的数字是ascending, 所以可以通过最后一个数//100算出树的深度
        self.mx = nums[n - 1] // 100
        
        # Calculate the size of the grid based on the maximum depth
        for i in range(self.mx - 1):
            siz *= 2
        
        # Initialize a grid with -1
        g = []
        for i in range(self.mx):
            row = []
            for j in range(siz):
                row.append(-1)
            g.append(row)
        
        # Fill the grid with values from nums
        for i in range(n):
            # Extract depth and position
            dep = nums[i] // 100
            pos = nums[i] // 10 % 10
            
            # Place the value in the grid
            g[dep - 1][pos - 1] = nums[i] % 10
        
        # Start DFS to calculate the path sums
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
        
        # Recursive DFS calls for left and right child nodes
        self.dfs(g, d + 1, 2 * p, sum)
        self.dfs(g, d + 1, 2 * p + 1, sum)

if __name__ == '__main__':
    ll = Solution()
    nums = [113, 215, 221]
    x = ll.pathSum(nums)
    print(x)
