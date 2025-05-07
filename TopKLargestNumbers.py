import heapq
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # 此题做法：用堆排序求出前K大数即可
        heapq.heapify(nums)

        # 这里调用.nlargest() method
        # k 表示几个数
        topk = heapq.nlargest(k, nums)
        
        #返回要找的几个数
        return topk

if __name__ =='__main__':
    ll = Solution()
    nums = [3, 10, 1000, -99, 4, 100]
    k = 3
    x = ll.topk(nums, k)
    print(x)
