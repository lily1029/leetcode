class Solution:
    """
    @param s: a string
    @return: nothing
    """
    def validPalindrome(self, s):
        left, right = self.twoPointer(s, 0, len(s) - 1) 
        #when it appears left >= right, it means it is an odd palindrome 
        #so, return True（且两边相等的以走完）
        if left >= right:
            return True
        
        # if left 还不大于right, we either move left one more, or move right to left one more   
        return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
    
    #if we get new left and right, we check it is palindrome or not 
    def isPalindrome(self, s, left, right):
        # we call twoPointer method to check it 
        left, right = self.twoPointer(s, left, right)
        
        # here if left >= right, here return True, otherwise , it return False
        return left >= right
        
    def twoPointer(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        return left, right
if __name__ == '__main__':
    ll = Solution()
    s = "abca"
    x = ll.validPalindrome(s)
    print(x)
