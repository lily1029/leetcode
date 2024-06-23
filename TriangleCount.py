class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # we need to sort list S first
        S.sort()
        
        # a global variable to count how many 
        # triangles
        ans = 0
        # go through c in list, takes O(n)
        for i in range(len(S)):
            #set two pointers 
            left, right = 0, i - 1
            while left < right:
                if S[left] + S[right] > S[i]:
                    # if satisfies above condition, 
                    # there are those number triangeles available 
                    ans += right - left
                    right -= 1
                else:
                    left += 1
        return ans
if __name__ == '__main__':
    ll = Solution()
    S = [3, 4, 6, 7]
    x = ll.triangleCount(S)
    print(x)
    