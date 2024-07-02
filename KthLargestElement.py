class Solution:
  
    def kthLargestElement(self, k, nums):
        # write your code here
        #use quickselect method, because it is ascending order, 
        # the kth largest number is len(nums) - k
        #e.g [2, 3, 4, 8, 9] time complexity: O(n)
        self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)
        return nums[len(nums) - k ]
    def quickSelect(self, nums, start, end, k):
        if  start >= end:
            return
        
        pivot = nums[(start + end) // 2]
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1 
            while left <= right and nums[right] > pivot:
                right -= 1 
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
        
        #at last, the right pointer is on the left part
        if k <= right:
            self.quickSelect(nums, start, right, k)
        #at last, the left pointer is on the right part
        if k >= left:
            self.quickSelect(nums, left, end, k)
if __name__ =='__main__':
    ll = Solution()
    k = 3
    nums = [9, 3, 2, 4, 8]
    x = ll.kthLargestElement(k, nums)
    print(x)