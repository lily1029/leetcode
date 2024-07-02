class Solution:
  
    def searchMatrix(self, matrix, target):
        """Binary search a ordered matrix, treat matrix as arrays"""
        if not matrix:
            return False
        
        #拿到row 和 col 的各自长度
        row, col = len(matrix), len(matrix[0])
        start, end = 0, row * col - 1  
         
        while start <= end:
            #用binary search, 找到中点
            mid = (start + end) // 2
            # 这里算row index and col index
            x, y = mid // col, int(mid % col) 
            num = matrix[x][y]
            
            #进行比较
            if num == target:
                return True
            elif num < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return False
if __name__ =='__main__':
    ll = Solution()
    matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
    ]
    target = 3
    x = ll.searchMatrix(matrix, target)
    print(x)