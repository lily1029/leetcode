class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        return self.divide_conquer(triangle, 0, 0, {})
        
    # 函数从坐标左上角（x, y）点出发，走到最底层的最短路径值
    # memo 中 key 为二元组 (x, y)
    # memo 中 value 为从 x, y 走到最底层的最短路径值
	# divideconquer + memo method
    def divide_conquer(self, triangle, x, y, memo):
        if x == len(triangle):
            return 0
            
        # 如果找过了，就不要再找了，直接把之前找到的值返回
        if (x, y) in memo:
            return memo[(x, y)]

        #divide part
        left = self.divide_conquer(triangle, x + 1, y, memo)
        right = self.divide_conquer(triangle, x + 1, y + 1, memo)
        
        # 在 return 之前先把这次找到的最短路径值记录下来
        # 避免之后重复搜索, conquer part
        memo[(x, y)] = min(left, right) + triangle[x][y]
        return memo[(x, y)]
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
    

