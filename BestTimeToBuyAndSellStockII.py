class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        
        if len(prices) <= 1:
            return 0

        #这里算股票最大利润    
        maxProfit = 0
        
        #go through 所有股票
        for i in range(0, len(prices) - 1):
            #并用当前天减去前一天的股票，看有没有利润
            if prices[i + 1] >  prices[i]:
                #如果有利润，计算利润
                maxProfit += prices[i + 1] - prices[i]
        return maxProfit
if __name__ == '__main__':
    ll = Solution()
    prices = [2, 1, 2, 0, 1]
    x = ll.maxProfit(prices)
    print(x)