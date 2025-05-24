class Solution:
  
    def kthLargestElement(self, k, nums):
        #use quickselect method, because it is ascending order, 
        # the kth largest number is len(nums) - k
        #e.g [2, 3, 4, 8, 9] time complexity: O(n)
        #这里找第几大的是从右往左数如果排好序，也可以是从左往右找第几小的数所以
        #是 len(nums)  - k
        self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)
        
        #返回要找的第几大数
        return nums[len(nums) - k ]
    
    #这里是用quickselect 算法
    def quickSelect(self, nums, start, end, k):

        #当start >= end时，说明两个指针已经相交相错了，返回
        if  start >= end:
            return 

            
        #用头指针和尾指针//2找到中间的pivot, 用这个pivot去partiton 
        #成2部分，小于pivot的到左边，大于pivot的到右边
        pivot = nums[(start + end) // 2]

        left, right = start, end

        while left <= right:

            while left <= right and nums[left] < pivot:

                left += 1 

            while left <= right and nums[right] > pivot:

                right -= 1 

            #这里找到不属于左边也不属于右边的，进行交换，然后两指针都向里走一步
            if left <= right:

                nums[left], nums[right] = nums[right], nums[left]

                left += 1 

                right -= 1 
        
        #at last, the right pointer is on the left part，recursively do left part
        if k <= right:
            self.quickSelect(nums, start, right, k)

        #at last, the left pointer is on the right part, recursively do the right part
        if k >= left:
            self.quickSelect(nums, left, end, k)
if __name__ =='__main__':
    ll = Solution()
    # k = 3
    # nums = [9, 3, 2, 4, 8]
    # k = 2
    # nums = [3, 2, 1, 5, 6, 4]
    k = 4
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    x = ll.kthLargestElement(k, nums)
    print(x)



