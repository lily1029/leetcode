DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    #这道题的做法就是从棋盘（board) 上第一个点出发上下左右四个点走， 
    #边走边看有没有这样的前缀出现， 如果有继续四个方向往下走， 
    #如果没有停止。 所以这道题变成了有没有某个前缀开头的单词
    def wordSearchII(self, board, words):
        #corner case
        if board is None or len(board) == 0:
            return []
        
        # pre-process
        # 预处理，把字典words里的单词进行前缀处理
        #这里是把words里的单词拆成，1个字母， 2个字母....的set
        #words = ["dog","dad","dgdg","can","again"]
        #word_set = {"dog","dad","dgdg","can","again"}
        #prefix_set =  {'d', 'do', 'dog', 'da', 'dad','dg', 'dgd',.....}
        word_set = set(words)
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])
        
        #从棋盘上第一个点进行search, 符合条件放入result中
        #i,j 代表横纵坐标
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                self.search(
                    board,
                    i,
                    j,
                    board[i][j],
                    word_set,
                    prefix_set,
                    set([(i, j)]),
                    result,
                )
                
        return list(result)
    
    #search方法定义， board是棋盘， x, y 是横纵坐标    
    def search(self, board, x, y, word, word_set, prefix_set, visited, result):
        #如果这个word不在prefix_set, 直接返回
        if word not in prefix_set:
            return
        
        #如果word在word_set里，加入到result里
        if word in word_set:
            result.add(word)
        
        #要查这个点的四个方向
        for delta_x, delta_y in DIRECTIONS:
            x_ = x + delta_x
            y_ = y + delta_y
            
            #查看这个新的点是否在棋盘里，有没有出了棋盘的边界
            #如果出了，就continue 剩下的代码
            if not self.inside(board, x_, y_):
                continue
            
            #如果这个新点没有出棋盘，看有没有被访问过了，如果有，
            #也要continue 剩下的代码
            if (x_, y_) in visited:
                continue
            
            #到这步说明它是一个没有出棋盘的点，也没有被访问过，放入
            #visited 集合里，并且对它进行search()method
            #这里最重要的是：word + board[x_][y_], e.g: do + g 
            #这里word 是 do， board[x_][y_] 是 g,对这个新的word进行dfs
            visited.add((x_, y_))
            self.search(
                board,
                x_,
                y_,
                word + board[x_][y_],
                word_set,
                prefix_set,
                visited,
                result,
            )
            #backtracking
            visited.remove((x_, y_))

    #这个method 判断是否出了棋盘的边界        
    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
    
if __name__ == '__main__':
    ll = Solution()
    board = ["doaf","agai","dcan"]
    words = ["dog","dad","dgdg","can","again"]
    # Output：["again","can","dad","dog"]
    # Explanation：
    #   d o a f
    #   a g a i
    #   d c a n
    # search in Matrix，so return ["again","can","dad","dog"].
    x = ll.wordSearchII(board, words)
    print(x)


