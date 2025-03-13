class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        #这里的index是从0开始，所以，要找kth smallest num 是 k-1
        self.quickSelect(nums, 0, len(nums) - 1, k - 1)
        return nums[k - 1]
    
    def quickSelect(self, nums, start, end, k):
        #当start == end时，说明两个指针已经相交找到第kth smallest number
        if start == end:
            return
        
        left, right = start, end
        pivot = nums[(left + right) // 2]
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # k在right的左边，recursively do left part       
        if k <= right:
            return self.quickSelect(nums, start, right, k)
        # k 在 left 的右边，recursively do right part
        elif k >= left: #and left <= end:
            return self.quickSelect(nums, left, end, k)
        
if __name__ =='__main__':
    ll = Solution()
    nums = [3, 4, 1, 2, 5]
    k = 3
    x = ll.kthSmallest(k, nums)
    print(x)


