class Solution:
    """
    直接模拟即可，读入字符串时按空格进行分隔，
    然后将分隔出的单词倒序输出
    """
    def reverseWords(self, str):
        # write your code here
        s = ""

        #pre is a left pointer
        n, pre = len(str), 0 

        #i is a right pointer, go through
        #the string and find space,add space
        #cut each word, at last reverse all
        for i in range(n + 1):
            if (i == n or str[i] == ' '):
                s += str[pre : i][: : -1]
                if i == n:
                    continue  
                s += " "
                pre = i + 1 
        return s[: : -1]
if __name__ =='__main__':
    ll = Solution()
    # str = "a b c"
    str = "the sky is blue"
    x = ll.reverseWords(str)
    print(x)