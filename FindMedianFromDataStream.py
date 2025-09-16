import heapq
class Solution:
    def __init__(self):
        #大顶堆放小于中位数的数，放加负号的数
        self.max_heap = []
        #小顶堆放大于中位数的数，在中位数的右边
        self.min_heap = []
        #最开始中位数是数据流中的第一个数
        #最开始加入的第一个数字，就是第一个中位数，因为只有一个
        self.is_first_add = True

    def add(self, val):
        if self.is_first_add:
            # 第一个进入数据流的数字是第一个中位数
            self.median = val
            #然后设置它为false
            self.is_first_add = False
            return

        #后又进的数val和中位数进行比较，如果小于中位数，加负号后放入max_heap
        if val < self.median:
            # 小的数放到大顶堆
            heapq.heappush(self.max_heap, -val)
        else:
            # 大于中位数的数放入min_heap中，保持原正数符号
            heapq.heappush(self.min_heap, val)

        # 比较两个heap的size，调整堆和中位数的位置,两边应该基本平衡
        #如果max_heap的长度大于min_heap,就将median推入min_heap
        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, self.median)
            #并且pop出max_heap中的最大数，并加上负号，使其恢复原始数
            self.median = -heapq.heappop(self.max_heap)

        #如果max_heap长度小于min_heap, 将median推入max_heap，并加负号
        if len(self.max_heap) < len(self.min_heap) - 1:
            heapq.heappush(self.max_heap, -self.median)
            #median就是min_heap pop出来的数
            self.median = heapq.heappop(self.min_heap)

    def getMedian(self):
        # 返回目前维护的中位数
        return self.median

if __name__ == '__main__':
    ll = Solution()
    #test data 1 
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

    #test data 2
    # ll.add(4)
    # x = ll.getMedian()
    # print(x)
    # ll.add(5)
    # y = ll.getMedian()
    # print(y)
    # ll.add(1)
    # z =ll.getMedian()
    # print(z)
    # ll.add(3)
    # q = ll.getMedian()
    # print(q)
    # ll.add(2)
    # w = ll.getMedian()
    # print(w)
    # ll.add(6)
    # a = ll.getMedian()
    # print(a)
    # ll.add(0)
    # b = ll.getMedian()
    # print(b)