DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    #此道题的做法是dfs在一个矩阵上面，从矩阵的（0，0）位置上开始dfs, dfs向
    #四个方向，上下左右，拿出矩阵中的点和word当中每个字母比对，如果一致，就说明
    #这个矩阵上有这个word,直到word结束
    def exist(self, board, word):
        # corner case, 空word, 返回true
        if not word:
            return True 
        
        #拿到矩阵的行数
        m = len(board)
        #拿到矩阵的列数
        n = len(board[0])
        #这里设置一个set(),避免重复搜索 
        visited = set()  

        #这里go through 整个矩阵，从（0，0）点开始，拿出每一个字母和word中的字母比对
        for i in range(m):
            for j in range(n):
                #这里检验这个字母是不是合法的，是不是和要搜索的word中的字母一样
                #如果都一样，返回true
                if self.dfs(i, j, word, 0, m, n, visited, board):
                    return True 
        #当矩阵全部走完后，走到这一步，说明这个board 里面没有这个word，返回false
        return False 

    #x,y 代表矩阵最左上角（0，0）点开始搜索，index是word中的index, m矩阵行数
    #n是矩阵列数，visited是set()，为避免重复搜索，board，题目给的棋盘    
    def dfs(self, x, y, word, index, m, n, visited, board):
        #如果走到这步，说明已经找到这个word在board上，返回true
        if index >= len(word):
            return True 
        
        #如果搜索的x, y，出了board 的边界，返回false
        if x >= m or x < 0 or y >= n or y < 0:
            return False 
        
        #如果（x, y)这个点已经被搜索过了， 返回false,避免重复搜索
        if (x, y) in visited:
            return False 

        #如果棋盘上的字母和word[index]所对应的字母不一样，返回false
        if board[x][y] != word[index]:
            return False 
       
       #到这一步，说明找到一个相同的字母对应的，所以放入它的矩阵坐标到set（）里
        visited.add((x, y))

        #对矩阵上的点进行四个方向搜索， DIR里有上下左右四个方向的坐标
        for dx, dy in DIR:
            #x, y 现在的这个点，dx, dy是DIR里方向的点，xx, yy是扩展后的点
            xx, yy = x + dx, y + dy 

            #对这个新的点进行dfs, 如果这个点合法，return true
            if self.dfs(xx, yy, word, index + 1, m, n, visited, board):
                return True 
        
        #如果不合法，remove掉这个点（x, y)
        visited.remove((x, y))

        #这个棋盘搜索完，还没有在上面的步骤返回true, 就证明这个board 里没有这个word,
        #返回false
        return False
    
if __name__ == '__main__':
    ll = Solution()
    board = ["ABCE","SFCS","ADEE"]
    word = "ABCCED"
    x = ll.exist(board, word)
    print(x)