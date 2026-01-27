# Method 1: 
# class Solution:
#     """
#     @param triangle: a list of lists of integers
#     @return: An integer, minimum path sum
#     """
#     def minimumTotal(self, triangle):
#         return self.divide_conquer(triangle, 0, 0, {})
        
#     # 函数从坐标左上角（x, y）点出发，走到最底层的最短路径值
#     # memo 中 key 为二元组 (x, y)
#     # memo 中 value 为从 x, y 走到最底层的最短路径值
# 	# divideconquer + memo method
#     def divide_conquer(self, triangle, x, y, memo):
#         if x == len(triangle):
#             return 0
            
#         # 如果找过了，就不要再找了，直接把之前找到的值返回
#         if (x, y) in memo:
#             return memo[(x, y)]

#         #divide part
#         left = self.divide_conquer(triangle, x + 1, y, memo)
#         right = self.divide_conquer(triangle, x + 1, y + 1, memo)
        
#         # 在 return 之前先把这次找到的最短路径值记录下来
#         # 避免之后重复搜索, conquer part
#         memo[(x, y)] = min(left, right) + triangle[x][y]
#         return memo[(x, y)]

# Method 2
# class Solution:
#     """
#     @param triangle: a list of lists of integers
#     @return: An integer, minimum path sum
#     """
#     def minimumTotal(self, triangle):
#         n = len(triangle)
        
#         # state: dp[i][j] 代表从(i,j)点走到最底层的最短路径值
#         dp = [[0] * (i + 1) for i in range(n)]
        
#         # initialize: 初始化终点值（最后一层）
#         for i in range(n):
#             dp[n - 1][i] = triangle[n - 1][i]
            
#         # function: 从下往上倒过来推导，计算每个坐标到哪儿去
#         # dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
#         for i in range(n - 2, -1, -1):
#             for j in range(i + 1):
#                 dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
                
#         # answer: 起点就是答案
#         return dp[0][0]

#滚动数组版本
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # 滚动数组版本
        n = len(triangle)
        #初始化两个滚动行，下行是由上行来，下行用完后在释放
        #出来，每行最长是n,所以初始化[0] * n 
        dp = [[0] * n, [0] * n]
        
        #滚动时候只要在行上模2就行
        #这里算最后一行的值
        for i in range(n):
            dp[(n - 1) % 2][i] = triangle[n - 1][i]
        
        #滚动时候只要在行上模2就行
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[i % 2][j] = min(dp[(i + 1) % 2][j], dp[(i + 1) % 2][j + 1]) + triangle[i][j]
        
        return dp[0][0]
    

if __name__ == '__main__':
    ll = Solution()
    triangle = triangle = [
                            [2],
                            [3,4],
                            [6,5,7],
                            [4,1,8,3]
                            ]
    x = ll.minimumTotal(triangle)
    print(x)
    

