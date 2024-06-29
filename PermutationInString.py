class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: if s2 contains the permutation of s1
    """
    def check_inclusion(self, s1: str, s2: str) -> bool:
        # write your code here
        n,m = len(s1), len(s2)
        if n > m: return False
        cnt1, cnt2 = [0]*26, [0]*26
        for i in range(n):
            cnt1[ord(s1[i])-ord('a')] += 1
            cnt2[ord(s2[i])-ord('a')] += 1
        if cnt1 == cnt2:
            return True
        for i in range(n,m):
            cnt2[ord(s2[i])-ord('a')] += 1
            cnt2[ord(s2[i-n])-ord('a')] -= 1
            if cnt1 == cnt2:
                return True
        return False
if __name__ == '__main__':
    ll = Solution()
    s1 = "ab" 
    s2 = "eidbaooo"
    x = ll.check_inclusion(s1, s2)
    print(x)

