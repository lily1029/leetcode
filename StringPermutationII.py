class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):

        #打乱成字符进行排序
        #先将字符串变成list, eg: "abb" => [a, b, b],
        #然后对list进行sort, 使相同的字母排在一起,以后好去重 eg: [a, b, b]
        chars = sorted(list(str))

        #这里用一个 boolean 数组来标识哪个字母先被选中进行dfs
        #所以初始值都为False eg: visited = [Fase, Fase, Fase]
        visited = [False] * len(chars)

        #这里存最终结果
        permutations = []

        #调用dfs
        self.dfs(chars, visited, [], permutations) 

        #返回结果
        return permutations

    def dfs(self, chars, visited, permutation, permutations):
        #递归出口， .join 操作产生一个新的字符串
        if len(chars) == len(permutation):
            permutations.append(''.join(permutation))
            return    
        
        #递归拆解， 这里的for 循环其实是选哪个字母为起始的字符串开头
        for i in range(len(chars)):
            #这里进行一个剪枝，如果已经用过的 visited[i] = true,直接跳过下面的代码
            if visited[i]:
                continue
            
            # a' a" b
            # => a' a" b => √
            # => a" a' b => x
            # 不能跳过一个a选下一个a, 如果i>0,而且i指的之母和前面的字母一样，
            #而且前面的已经被选过，visit[i-1]=false,表示被选过，这里要进行剪枝，直接跳过相同的字母,continue
            #注意这里 not  visited[i - 1] 
            #这里 not Fase = true, 所以前一个被选过的是 visit[i-1]= False
            if i > 0 and chars[i] == chars[i - 1] and not  visited[i - 1]:
                continue
            
            # make changes，先选哪个字母，它所对应的visited[i]= True,然后放到permutation中，
            #之后变成一个串
            visited[i] = True
            permutation.append(chars[i])
            
            # 找到所有 permutation 开头的排列
            # 找到所有 "a" 开头的permutation, 找到所有以"b"开头的permutation,....
            self.dfs(chars, visited, permutation, permutations)
            
            # backtracking 后，permutation变空，并且恢复False,又可以进行新的dfs搜索
            permutation.pop()
            visited[i] = False

if __name__ == '__main__':
    ll = Solution()
    s = "abb"
    x = ll.stringPermutation2(s)
    print(x)