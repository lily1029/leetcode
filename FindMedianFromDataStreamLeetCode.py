import heapq
class MedianFinder:
    def __init__(self):
        self.lo = []  
        self.hi = []  

    def addNum(self, num):
        heapq.heappush(self.lo, -num)             # lo is maxheap, so -1 * num
        heapq.heappush(self.hi, -self.lo[0])      # hi is minheap
        heapq.heappop(self.lo)
        
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -self.hi[0])
            heapq.heappop(self.hi)
            
    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]                  
        else:
            return (self.hi[0] - self.lo[0]) / 2  # - as low has -ve values

if __name__ == '__main__':
    ll = MedianFinder()
    ll.addNum(1)
    x = ll.findMedian()
    print(x)
    ll.addNum(2)
    y = ll.findMedian()
    print(y)
    ll.addNum(3)
    z = ll.findMedian()
    print(z)
    ll.addNum(4)
    q = ll.findMedian()
    print(q)
    ll.addNum(5)
    w = ll.findMedian()
    print(w)