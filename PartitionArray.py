class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        #first element and the last element
        left, right = 0, len(nums) - 1
        
        #while 循环，只要left <= right
        while left <= right:
            #只要满足左边的数小于k， left + 1
            while left <= right and nums[left] < k:
                left += 1
            #只要满足右边的数大于等于k， 右指针-1
            while left <= right and nums[right] >= k:
                right -= 1

            #此时左右两数进行交换， 并且两支针个向前中间走一步
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        #因为left 多走一步，所以left就是它们分割点
        return left
if __name__ == '__main__':
    ll = Solution()
    nums = [3, 2, 2, 1]
    k = 2
    x = ll.partitionArray(nums, k)
    print(x)

  