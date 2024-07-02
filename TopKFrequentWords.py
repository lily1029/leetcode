class Solution:
    
    def topKFrequentWords(self, words, k):
        # write your code here
        if not words or not k:
            return []
        
        from heapq import heappush, heappop
        dict = {}

        #记录words中的单词数量
        for word in words:
            if word in dict:
                dict[word] += 1 
            else:
                dict[word] = 1
              
        #定义一个min heap, 弹出的都是heap中最小的
        heap = []
        for word in dict:
            heappush(heap, (-dict[word], word))
    
        #弹出前k个
        ans = []
        for word in range(k):
            num, word = heappop(heap)
            ans.append(word)
        return ans
if __name__ =='__main__':
    ll = Solution()
    words = [1, 1, 1, 2, 2, 3]
    k = 2
    x = ll.topKFrequentWords(words, k)
    print(x)