class Solution:
    """
    从左下角开始，往右上角逼近
    从左下角即(n-1,0)处出发
    """
    def searchMatrix(self, matrix, target):
        # initialize corner cases 
        if not matrix:
            return 0
        
        # initialize rows and columns  
        row, column = len(matrix), len(matrix[0])
        # we start it from the left bottom corner
        i, j = row - 1, 0
        count = 0
        while i >= 0 and j < column:
            if matrix[i][j] == target:
                count += 1
                i -= 1
                j += 1
            # for this smaller case, we move it right one step
            #如果matrix[x][y] < target 下一步往右搜,所以 j +=1
            elif matrix[i][j] < target:
                j += 1
            # if it is bigger, we move upper one row 
            #如果matrix[x][y] > target 下一步往上搜,所以,用i -=1,因为在往下数字会更大
            elif matrix[i][j] > target:
                i -= 1
        # finally, we return the count 
        return count
if __name__ =='__main__':
    ll = Solution()
    matrix = [
      [1, 3, 5, 7],
      [2, 4, 7, 8],
      [3, 5, 9, 10]
    ]
    target = 3
    x = ll.searchMatrix(matrix, target)
    print(x)