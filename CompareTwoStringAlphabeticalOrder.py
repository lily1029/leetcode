class Solution:

    def funcAlphabeticOrder(self, s):
        for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                return i
        
        return 0

if __name__ == '__main__':
    ll = Solution()
    y = "adha"
    x = ll.funcAlphabeticOrder(y)
    if x == 0:
        print(0)
    else:
        print(x + 1)


