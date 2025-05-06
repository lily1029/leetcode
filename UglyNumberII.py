import heapq

class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):

        #我们用一个heap来放第一个初始的ugly number: 1
        heap = [1]

        #用一个集合来进行标识，以免有重复的
        visited = set([1])
        
        # val 表示heap里存放的数字，初始值为None
        val = None

        #go through ugly number从1-9
        for i in range(n):
            #将现有在heap里的丑数pop出，依次与2，3，5
            #相乘，看看在不在visited set里，如果不在放入heap中
            #在heap中依次弹出的数就是第一个，第二个....直到第n个数
            val = heapq.heappop(heap)

            #将现有在heap里的丑数pop出，依次与2，3，5想乘
            for factor in [2, 3, 5]:
                #看看相乘后的积在不在visited set 里，不在，放入
                if val * factor not in visited:
                    visited.add(val * factor)
                    #并且push到heap里
                    heapq.heappush(heap, val * factor)

        #这里go through 完第几个number的循环后，在heap里弹出的就是第几数    
        return val
			
if __name__ == '__main__':
    ll = Solution()
    n = 9 
    x = ll.nthUglyNumber(n)
    print(x)