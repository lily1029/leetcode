class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        这道题做法是：从右往左遍历s,遇到space往左
        碰到单词开始记录长度，直到最后一个单词结束
        """
        # write your code here
        if not s: 
            return 0
        
        #从字符串末尾开始指针
        index = len(s) -1

        #当末尾是space, 指针向左一个
        while s[index] == " ":
            index -= 1
        
        #这里算最后一个word的长度   
        wordLength = 0    

        #当index还没走到最左边，并且指的不是空
        while index >= 0 and s[index] != ' ':
            #说明找到了最后一个word,记录它的长度
            wordLength += 1
            #指针继续向左
            index -= 1

        #返回最后一个word 的长度
        return wordLength

if __name__ =='__main__':
    ll = Solution()
    s = "   fly me   to   the moon  "
    x = ll.lengthOfLastWord(s)
    print(x)