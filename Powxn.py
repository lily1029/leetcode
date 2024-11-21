class Solution:
    """
    @param x: the base number
    @param n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        if abs(n) > 1:    
            if n % 2 == 0:
                #这里进行二分
                temp = self.myPow(x, n//2)
                return temp * temp
            if n % 2 != 0:
                temp = self.myPow(x, n//2)
                return temp * temp * x
if __name__ =='__main__':
    ll = Solution()
    x = 2
    n = 3
    y = ll.myPow(x, n)
    z = print(y)