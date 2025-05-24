import heapq
class Solution:
    def __init__(self):
        # 小顶堆放大于中位数的数
        # 大顶堆放小于中位数的数
        # 最开始中位数是数据流中的第一个数
        self.max_heap = []
        self.min_heap = []
        self.is_first_add = True

    def add(self, val):
        if self.is_first_add:
            # 第一个进入数据流的数字是第一个中位数
            self.median = val
            self.is_first_add = False
            return
    
        if val < self.median:
            # 小的数放到大顶堆
            heapq.heappush(self.max_heap, -val)
        else:
            # 大的数放到小顶堆
            heapq.heappush(self.min_heap, val)

        # 比较堆中数字数量，调整堆和中位数
        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, self.median)
            self.median = -heapq.heappop(self.max_heap)
        if len(self.max_heap) < len(self.min_heap) - 1:
            heapq.heappush(self.max_heap, -self.median)
            self.median = heapq.heappop(self.min_heap)

    def getMedian(self):
        # 返回目前维护的中位数
        return self.median

if __name__ == '__main__':
    ll = Solution()
    ll.add(1)
    x = ll.getMedian()
    print(x)
    ll.add(2)
    y = ll.getMedian()
    print(y)
    ll.add(3)
    z = ll.getMedian()
    print(z)
    ll.add(4)
    q = ll.getMedian()
    print(q)
    ll.add(5)
    w = ll.getMedian()
    print(w)