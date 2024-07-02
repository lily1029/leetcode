import heapq
class Solution:
     def findKthSmallest(self, nums, k):
         # 1: Create max heap (simulated by negative values)
         #so, max_heap is like [-6, -5, -4, -3], then pop -6
         #O(nlogk)
         max_heap = []

         #go through each element in nums       
         for element in nums:
             
             # 2: Insert each element to the heap
             heapq.heappush(max_heap, -element)
             # 3: If the size of the heap exceeds k, 
             #pop the element at the top, 
             #which is not kth element
             if len(max_heap) > k:
                 heapq.heappop(max_heap)
         
         # 4: return top element of max heap
         return -heapq.heappop(max_heap)

if __name__ =='__main__':
    ll = Solution()
    nums = [1, 5, 7, 6, 4, 3]
    k = 3
    x = ll.findKthSmallest(nums, k)
    print(x)