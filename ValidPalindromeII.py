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

    #这里其实是two pointer算法， 设最左边一个指针，最右边一个指针，然后在左边<右边的情况下，比较这两个字母是不是
    #一样，不一样，返回这left 和right的位置，然后要不然去掉left一个字母或是去掉right字母看能不能成valid palindrome   
    def twoPointer(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right

            #如果left 和right 一样，left往前一个，right退后一个
            left += 1
            right -= 1

        #返回这个left 和right 的位置
        return left, right
if __name__ == '__main__':
    ll = Solution()
    s = "abca"
    x = ll.validPalindrome(s)
    print(x)




