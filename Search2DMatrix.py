class Solution:
  
    def searchMatrix(self, matrix, target):
        """Binary search a ordered matrix, treat matrix as arrays"""
        if not matrix:
            return False
        
        #拿到row 和 col 的各自长度
        row, col = len(matrix), len(matrix[0])
        #如果想把它做成arry的长度算，row*col-1
        #array starts at 0 position
        start, end = 0, row * col - 1  
         
        while start <= end:
            #用binary search, 找到中点
            mid = (start + end) // 2
            # 这里算row index and col index
            #The row is found using integer division: mid // col.
            #The column is found using the modulus operator: mid % col.
            x, y = mid // col, int(mid % col) 
            num = matrix[x][y]
            
            #进行比较
            if num == target:
                return True
            #这里如果num小于target,扔掉mid左边的所有数，并从mid + 1开始继续
            #二分查找
            elif num < target:
                start = mid + 1
            #反之，如果num大于target,缩小end 的距离，到end = mid -1
            else:
                end = mid - 1
        
        #如果for 循环所有情况后，还没有，返回false
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




