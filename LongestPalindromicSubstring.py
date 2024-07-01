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
        #define a result string 
        longest = ""

        #we go through the string to find the middle 
        # in order to proceed the longest one
        for mid in range(len(s)):
            # when the string is odd length
            sub = self.is_palindrom(s, mid, mid)
            #if find the sub string is longer 
            #than the global string (longest)
            if len(sub) > len(longest):
                longest = sub
            
            # when the string is even length
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


