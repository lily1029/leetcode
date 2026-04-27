
class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, source, pattern):
        return self.is_match_helper(source, 0, pattern, 0, {})     
    
        
    # source 从 i 开始的后缀能否匹配上 pattern 从 j 开始的后缀
    # 能 return True, 不能，return false
    def is_match_helper(self, source, i, pattern, j, memo):
        #先看看是否已经存在了字典里，如果存了，直接拿出来，不用二次搜索
        if (i, j) in memo:
            return memo[(i, j)]
        
        # source is empty,当source都走到后面没有了，成空串了，source 和target 匹配到后面都是空串了，返回true
        #这里是这个意思： source 已经全部用完了（也就是走到结尾了），那么如果pattern 有剩下的部分，看它能不能变成
        #空串，如果能，说明它们match, 返回true, otherwise, 返回false. e.g : source = "" pattern = "a*b*c*"
        #每个*都可以取0次，所以 a* -> "", b* ->"", c* -> "", 最终return true
        #If the source is empty, we check whether the remaining pattern can match an empty string.
        if len(source) == i:
            return self.is_empty(pattern[j:])

        #这句话的意思是，如果pattern 用完了，但是source还有东西，说明不匹配，return false
        #因为pattern 已经空了， 不可能匹配任何字符串了 
        #这里核心要记住：source 空了， 看pattern 还能不能变空
        #但是如果pattern空了， 如果source 还有， 一定不行 ！   
        if len(pattern) == j:
            return False
        
        #这里要注意：这里的*不代表任意字符串，而是代表*前的字母出现0次或是多次，e.g: c*,
        #如果想表示任意字符串这里要用.* 这里的.*代表可以匹配任何字符串，比如可以匹配abcdefg 等等
        #所以做这个题也是从头往后 source 和pattern 进行比较，就是这里不是看第一个字符， 
        #而是看第二个字符是不是*
        # j + 1 < len(pattern) 表示：首先看看pattern里有没有第二个字符
        # 在看看第二个字符是不是* pattern[j + 1] == '*'
        # 下面的条件就是，如果有第二个字符，而且是*
        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            #我们先比较source 和 target的第一个字符是不是一样 用（.is_match_char（） method）， 比如：source = caabb, target = c*a*b 
            #这里当它们第一个字符相等都是c,
            #并且这时把source 中的第一个c吃掉（i + 1），后，在比较剩下的， 这时候 source = aabb  target = c*a*b 或者是第二种情况
            #一个都没有吃source, 所以就把 j+2 ,pattern 直接去掉，匹配一个0 source 字符串，在继续比较，这时变成
            #source = aabb  target = a*b 继续进行比较
            #所以下面的情况就是c* 吃source 一个： i + 1， c* 完全不吃，匹配0字符串， j + 2
            matched = self.is_match_char(source[i], pattern[j]) and self.is_match_helper(source, i + 1, pattern, j, memo) or \
            self.is_match_helper(source, i, pattern, j + 2, memo)
        else: 
            #如果不是*，这里是判断source 和 target 的首字母首先要相等， i， j, 然后各自加一 i + 1, j + 1 , 继续比较下面的               
            matched = self.is_match_char(source[i], pattern[j]) and self.is_match_helper(source, i + 1, pattern, j + 1, memo)
        
        memo[(i, j)] = matched
        return matched
        
        
    def is_match_char(self, s, p):
        return s == p or p == '.'

    #这个method 是在check 这个pattern 是不是空串 ？     
    def is_empty(self, pattern):
        #如果pattern 的长度 对2 取模 后等于 1， 说明它不是空串，return false
        #合法长度必须是偶数，奇数不行
        if len(pattern) % 2 == 1:
            return False
        
        #如果pattern 的长度取模后不等于1，这时后就要看看它是否可以变成空串，因为合法的结构是 （字符 + *）（字符 + *）（字符 + *）
        #每组占2个字符，所以长度必须是偶数，如果是奇数，一定有一组是没有*的。
        #这个for 循环就是在检查每一对是不是（字符 + *） e.g: x*
        for i in range(len(pattern) // 2):
            #这里检查每一组的第二个字符是不是*
            if pattern[i * 2 + 1] != '*':
                #如果不是*，则返回false
                return False
        #到这一步说明是个合法的，返回true
        return True
        #conclusion: a pattern can match an empty string only if it consists of pairs like x*
        #so we check that the length is even and every second charcter is *

if __name__ == '__main__':
    ll = Solution()
    source = "caab"
    pattern = "c*a*b"
    x = ll.isMatch(source, pattern)
    print(x)
    
    