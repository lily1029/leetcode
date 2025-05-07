import heapq

class Solution:
    # @param {int} k an integer
    # k 代表 k 个top largest numbers   
    def __init__(self, k):
        # k 代表heap 中放几个数，是heap的长度
        self.k = k
        # 初始化一个minheap
        self.heap = []
        
    # @param {int} num an integer
    def add(self, num):
        #把这个num, push 到min heap 中
        heapq.heappush(self.heap, num)
        
        #如果heap的长度超过了k个，就pop出去
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

    # @return {int[]} the top k largest numbers in array
    def topk(self):
        return sorted(self.heap, reverse=True)

if __name__ =='__main__':
    s = Solution(3)
    s.add(3)
    s.add(10)
    s.topk()
    s.add(1000)
    s.add(-99)
    s.topk()
    s.add(4)
    s.topk()
    s.add(100)
    s.topk()
    print(s.topk())
