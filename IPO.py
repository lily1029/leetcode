from typing import (
    List,
)
from heapq import *

class Solution:
    def find_maximized_capital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #如果当前资金 w 已经大于等于所有项目的最低资金需求，
        #说明所有项目都能做，直接从所有利润中选最大的 k 个加起来返回
        if w >= max(capital):
            return w + sum(nlargest(k, profits))

        #项目总数
        n = len(profits)

        # 指针：记录下一个待处理的项目索引
        curr = 0

        #这里整合每一个capital 对应的profit,把它写在一起
        # capital = [0, 1, 1]
        # profits = [1, 2, 3]
        #整合成 arr= [(0, 1), (1, 2), (1, 3)]
        # 把每个项目的 (最低资金, 利润) 打包成元组列表
        arr = [(capital[i], profits[i]) for i in range(n)]

        #要想启动这个项目，根据capital进行从小到大的sort
        #这里面是用到了lambda表达式，lambda表达式就是没有名字的函
        arr.sort(key = lambda x : x[0])
        
        #这里定义一个priority queue
        # 最大堆（用负数模拟，因为 Python 的 heapq 是最小堆）
        pq = []

        #这里for 循环最多k个项目. 
        for _ in range(k):
            # 把所有当前资金 w 能负担得起的项目，加入堆中
            # （即 capital <= w 的项目全部解锁）
            while curr < n and arr[curr][0] <= w:
                # 存负数，让利润最大的排在堆顶
                heappush(pq, -arr[curr][1])
                curr += 1
            #当priority queue不为空时，弹出里面的profit, 
            #并和初始的w想加，这是完成一个项目后，挣得profit
            if pq: 
                # 从堆中取出利润最大的项目（取负数还原），加到资金中
                # heappop 取出最小值（即负的最大利润），减负得正
                w -= heappop(pq)
            else:
                # 堆为空，说明没有能做的项目了，提前退出
                break
        
        # 返回最终最大化的资本
        return w

if __name__ == '__main__':
    ll = Solution()
    k=2
    W=0
    Profits=[1,2,3]
    Capital=[0,1,1]
    x = ll.find_maximized_capital(k, W, Profits, Capital)
    print(x)

    



