class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    #这个题的做法：就是拿pattern 的一个字母和string 里的
    #不同长度的字符串 一个一个对应的去试着匹配。
    def wordPatternMatch(self, pattern, string):
        
        #这里其实是call dfs() 算法
        return self.is_match(pattern, string, {}, set())

    def is_match(self, pattern, string, mapping, used):

        if not pattern:
            return not string
        
        #先拿到pattern[0]的第一个字符，然后看看它之前有没有出现过，   
        char = pattern[0]

        #如果已经在mapping里
        if char in mapping:
            #拿出这个字符，放入到word里
            word = mapping[char]
            #如果对应的字符串开头不是word, 说明不匹配，return False
            if not string.startswith(word):
                return False
            #否则说明匹配，在往下递归
            return self.is_match(pattern[1:], string[len(word):], mapping, used)
        
        #这里查看pattern应该对应哪个字符串(string)    
        for i in range(len(string)):

            #比如当前word对应这个位置
            word = string[:i + 1]

            #如果word已经在used里, 说明这个string已经在之前进行过匹配，需要continu
            #因为这里是进行新string的匹配
            if word in used:
                continue
            
            #如果没有在used中出现，要进行新的匹配，直接加到used中，同时放入mapping
            used.add(word)
            mapping[char] = word
            
            #继续往下递归
            if self.is_match(pattern[1:], string[i + 1:], mapping, used):
                return True
            
            #如果以上递归return False,我们需要回溯
            del mapping[char]
            used.remove(word)
        
        #如果所有走完都找不到匹配，我们return False, 说明没有匹配   
        return False
    
if __name__ == '__main__':
    ll = Solution()
    # pattern = "abab"
    # str = "redblueredblue"
    pattern = "abab"
    str = "redred"
    x = ll.wordPatternMatch(pattern, str)
    print(x)

