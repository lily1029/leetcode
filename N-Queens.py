#解法: 就是用DFS做， 比如皇后放到0列，是可以的，然后下一行，看皇后放哪，
#可以满足不和第一个皇后攻击，
class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        #result用于存储答案
        results = []

        #调用dfs 
        self.search(n, [], results)
        return results
    
    #search函数为搜索函数，n表示已经放置了n个皇后，col表示每个皇后所在的列
    def search(self, n, col, results):

        #这里根据col的长度放好后 ，延伸下一个row 的位置
        row = len(col)

        #若已经放置了n个皇后表示出现了一种解法，绘制后加入答案result
        if row == n:
            results.append(self.Draw(col))
            return
        
        #枚举当前皇后固定在row行时，应该放置的列，若不合法则跳过，
        #列从0，开始，一直到列的末尾, now_col表示现在正在放的col
        for now_col in range(n):
            #check 现在放的queen 在这个row, 和这个now_col是否valid
            if not self.isValid(col, row, now_col):
                continue

            #若合法则,放入该queen, 然后继续递归枚举下一行的皇后
            col.append(now_col)
            self.search(n, col, results)
            col.pop()

    #isValid函数为合法性判断函数
    def isValid(self, cols, row, now_col):
        #这里r, c代表之前放好的queen的行和列的位置，
        # 一个一个循环之前queens的位置
        for r, c in enumerate(cols):
            #若有其他皇后在同一列或同一斜线上则不合法, 
            #c是queen所在的列， 不可在同一个列上，
            if c == now_col:
                return False
            
            # r, c 是之前的queen所在的行和列
            #若有其他皇后在同一斜线上则不合法,
            if abs( r - row ) == abs( c - now_col ):
                return False
        #到这一步，表示这个queen是 valid, 返回true
        return True
    
    #Draw函数为将col数组转换为答案的绘制函数
    def Draw(self, cols):
        n = len(cols)
        board = []
        for i in range(n):
            row = ['Q' if j == cols[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board
		#	Time Complexity: s * n^2

if __name__ == '__main__':
    ll = Solution()
    n = 4
    x = ll.solveNQueens(n)
    print(x)


