class Solution:
    """
    此题思路是从s的两边用2个指针进行两边比较，相同
    继续，不同，就不是，这里要跳过特殊字符和空格
    """
    def is_palindrome(self, s: str) -> bool:
        # write your code here
        #i 为头指针，j 为尾指针
        i , j = 0, len(s) - 1

        #while循环，头尾进行比较
        while i < j:
            #.isalnum(). This method means 
            #returns True if all the characters 
            #are alphanumeric, meaning alphabet 
            #letter (a-z) and numbers(1-9).
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            #if two ends are all valid characters, 
            #we need to change both to #lower case
            if s[i].lower() != s[j].lower():
                return False
            i += 1 
            j -= 1
        return True 
if __name__ == '__main__':
    ll = Solution()
    s = "a,bcb a"
    x = ll.is_palindrome(s)
    print(x)
