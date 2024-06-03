class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return ""
        
        sub = ""
        longest = ""

        for mid in range(len(s)):
            sub = self.is_palindrom(s, mid, mid)
            if len(sub) > len(longest):
                longest = sub
            
            sub = self.is_palindrom(s, mid, mid + 1)
            if len(sub) > len(longest):
                longest = sub
        return longest 
   
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


