class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, source, pattern):
        #调用helper函数
        return self.is_match_helper(source, 0, pattern, 0, {})
        
        
    # source 从 i 开始的后缀能否匹配上 pattern 从 j 开始的后缀
    # 能 return True, 这里变成从i和j后面的子串
    def is_match_helper(self, source, i, pattern, j, memo):
        #memoization
        if (i, j) in memo:
            return memo[(i, j)]
            
        #如果source是空,pattern里必须全部是空，否则return False
        #如果走到source是空的位置，pattern对应的必须是*，要不然false
        if len(source) == i:
            # every character should be "*"
            for index in range(j, len(pattern)):
                if pattern[index] != '*':
                    return False
            return True
        
        #如果source非空，但是pattern空，肯定不匹配，return False    
        if len(pattern) == j:
            return False
        
        #如果pattern的第一个字母不是*,就先比较两个字符串的第一个字符，如果第一个字符
        #相等，比较第二个字符，并存入memo中
        if pattern[j] != '*':
            matched = self.is_match_char(source[i], pattern[j]) and \
                self.is_match_helper(source, i + 1, pattern, j + 1, memo)
        else:  
            #i + 1 代表*号吃掉至少一个character，或是更多都可以因为*匹配字符串
            #*号匹配至少一个character,或是2, 3, 4 characters，此时的pattern 不变
            #pattern不变是因为还可以吃更多的characters....
            #也相当于这里的条件是不吃空字符，吃至少一个以上的characters
            matched = self.is_match_helper(source, i + 1, pattern, j, memo) or \
                self.is_match_helper(source, i, pattern, j + 1, memo)
                 # j + 1 代表*不吃任何字符(只吃了一个空字符），*匹配一个空character
                 # 所以i不变，空字符不算长度，所以i不变
        
        #存入每次匹配的值，并且返回
        memo[(i, j)] = matched
        return matched
        
    #这里判断2个字符串的第一个字母是否一致，或是？可以匹配任意一个character 
    def is_match_char(self, s, p):
        return s == p or p == '?'

if __name__ == '__main__':
    ll = Solution()
    s = "abb"
    p = "?*"
    # s = "abbcd"
    # p = "a*b*"
    x = ll.isMatch(s, p)
    print(x)
 




