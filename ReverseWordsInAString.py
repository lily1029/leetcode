class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code
        #strip()去掉s头尾的空格，split()按照空格分割字符串，reversed翻转，''.join按照空格连接字符串
        return ' '.join(reversed(s.strip().split()))
if __name__ =='__main__':
    ll = Solution()
    s = "the sky is blue"
    x = ll.reverseWords(s)
    print(x)
        