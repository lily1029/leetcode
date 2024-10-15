class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return ""
        
        #这里找到sub string 中找到符合题意要求的string
        sub = ""
        #这里找最长的sub string
        longest = ""

        #这里的idea是一个一个字符切割，当是奇数string,由中间的向两边两个
        #指针进行比较，如果是偶数长度string,左右两边进行比较
        #所以这里要go through整个string一遍，time: O(n)
        for mid in range(len(s)):
            #odd string, 所以从中间开始阔，mid中间值一样
            sub = self.is_palindrom(s, mid, mid)
            #if find the sub string is longer 
            #than the global string (longest)
            if len(sub) > len(longest):
                longest = sub
            
            #even string,指针在中间，左右两边差1
            sub = self.is_palindrom(s, mid, mid + 1)
            if len(sub) > len(longest):
                longest = sub
        return longest 
   
   #here to compare left and right to see if it is a palindrome
    def is_palindrom(self, string, left, right):
        while left >= 0 and right < len(string):
            if string[left] != string[right]:
                break 
            
            left -= 1 
            right += 1 
        return string[left + 1 : right]
if __name__ =='__main__':
        solution = Solution()
        s = "acdcb"
        x = solution.longestPalindrome(s)
        print(x)


