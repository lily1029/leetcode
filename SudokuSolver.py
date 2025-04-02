# 此题解法：
# 就是从棋盘第一个数往下枚举， 一个一个试，直到满足整个board. 
class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """
    def solveSudoku(self, board):

        self.backtrack(board, 0, 0)

        return board
    
    def backtrack(self, board, i, j):
        m, n = 9, 9

        # 到达第n列，越界，换到下一行第0列重新开始
        if j == n:
            return self.backtrack(board, i + 1, 0)
        
        # 到达第m行，说明找到可行解，触发 base case
        if i == m:
            return True
        
        # 如果有预设数字，不用我们穷举直接下一个j+1
        if board[i][j] != 0:
            return self.backtrack(board, i, j + 1)
        
        #从board的(0,0)开始从1 开始试直到9
        for val in range(1, 10):

            # 如果遇到不合法的数字，就跳过
            if not self.isValid(board, i, j, val):
                continue

            # 经过验证，可以确定的一个数字
            board[i][j] = val
            
            # 如果找到一个可行解，立即结束
            # 找完上一个后，找同行的下一个点j+1 
            # 这一行,列(i, j+1)都满足条件下返回True 
            if self.backtrack(board, i, j + 1):
                return True
            
            #否则，撤回选择，从board[i][j] = 0重新换数
            board[i][j] = 0

        # 穷举完1~9，依然没有找到可行解，此路不通
        return False
    
    def isValid(self, board, row, col, val):

        for i in range(9):
            # 判断行是否存在重复
            if board[row][i] == val:
                return False
            
            # 判断列是否存在重复
            if board[i][col] == val:
                return False
            
            # 判断 3 x 3 方框是否存在重复
            if board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] == val:
                return False
            
        return True

if __name__ == '__main__':
    ll = Solution()
    board = [[0,0,9,7,4,8,0,0,0],
            [7,0,0,0,0,0,0,0,0],
            [0,2,0,1,0,9,0,0,0],
            [0,0,7,0,0,0,2,4,0],
            [0,6,4,0,1,0,5,9,0],
            [0,9,8,0,0,0,3,0,0],
            [0,0,0,8,0,3,0,2,0],
            [0,0,0,0,0,0,0,0,6],
            [0,0,0,2,7,5,9,0,0]]
    
    x = ll.solveSudoku(board)
    print(x)
            
            