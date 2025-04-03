
class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    #此题就是为每一个pattern中的字符找到唯一的映射，
    #且为teststr中每一个字符串找到唯一的映射。映射我们可以通过
    #数据结构Map或者dict来实现。重点在于每个字符有且只有一个映射。
    # test data: pattern = "abba", str = "dog cat cat dog"
    
    def wordPattern(self, pattern, teststr):
        #这里是pattern 里的字符 对string 的映射
        #pattern_to_str: {'a' : 'dog', 'b' : 'cat'}
        pattern_to_str = {}

        #这里是string 对 pattern中的字符的映射
        #str_to-pattern: {'dog' : 'a', 'cat': 'b'}
        str_to_pattern = {}

        #这里split()后，变成：strs: ['dog', 'cat', 'cat', 'dog']
        strs = teststr.split()
        
        #这里先设match 为true,如果false,在后面code 中return false
        match = True
        
        #循环pattern的长度，找pattern中对应的 string
        for i in range(len(pattern)):
            #拿到每一个pattern 字母 e.g: pattern_char = a
            pattern_char = pattern[i]

            #拿到和pattern i 对应的位置的string
            str = strs[i]
            
            # 如果pattern_char 不在pattern_to_str字典中，加入字典，尝试匹配；
            if pattern_char not in pattern_to_str:
                pattern_to_str[pattern_char] = str

            #如果冲突则不匹配, 如果pattern_char 对应的字母不和string匹配
            # make  match = false, 并且 break    
            elif pattern_to_str[pattern_char] != str:
                match = False
                break
            
            # 如果str不在str_to_pattern字典中，加入字典进行匹配；
            if str not in str_to_pattern:
                str_to_pattern[str] = pattern_char
            
            #如果冲突则不匹配，同上
            elif str_to_pattern[str] != pattern_char:
                match = False
                break
        
        #如果在上面的过程中都没有走到  match = false
        #说明match = true, 匹配成功
        return match

if __name__ == '__main__':
    ll = Solution()
    pattern = "abba" 
    str = "dog cat cat dog"
    x = ll.wordPattern(pattern, str)
    print(x)
