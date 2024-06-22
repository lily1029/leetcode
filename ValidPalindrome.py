class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def is_palindrome(self, s: str) -> bool:
        # write your code here
        i , j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
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
