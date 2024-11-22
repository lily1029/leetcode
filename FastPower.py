class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # 任何数的 x^0 = 1, 所以是1%b
        if n == 0:
            return 1 % b
    
        #这里二分指数
        if n % 2 == 0:
            tmp = self.fastPower(a, b, n // 2)
            return tmp * tmp % b
        else:
            tmp = self.fastPower(a, b, n // 2)
            return tmp * tmp * a % b
if __name__ =='__main__':
    ll = Solution()
    a = 3
    b = 7
    n = 5
    x = ll.fastPower(a, b, n)
    print(x)
    