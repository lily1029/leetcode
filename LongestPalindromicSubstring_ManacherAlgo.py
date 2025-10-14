class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longestPalindrome(self, s) -> str:
        # Transform the string
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0  # center and right edge
        for i in range(1, n-1):
            mirr = 2*C - i  # mirror of i around center C
            if i < R:
                P[i] = min(R - i, P[mirr])
            
            # Attempt to expand palindrome centered at i
            while T[i + (1 + P[i])] == T[i - (1 + P[i])]:
                P[i] += 1
            
            # Update center and right edge if expanded past R
            if i + P[i] > R:
                C, R = i, i + P[i]
        
        # Find the maximum length palindrome
        max_len, center_index = max((n, i) for i, n in enumerate(P))
        start = (center_index - max_len) // 2  # index in original string
        return s[start:start + max_len]

if __name__ =='__main__':
        solution = Solution()
        # s = "acdcb"
        s = "cdc"
        x = solution.longestPalindrome(s)
        print(x)


