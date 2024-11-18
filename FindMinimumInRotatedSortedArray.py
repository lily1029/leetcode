class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        #做这道题首先要将数据矩形化，然后， 因为要找最小的
        #所以我们在找右下角那段,做二分的区间在（nums[mid], nums[end])
        if not nums:
            return -1
        start, end = 0, len(nums) - 1 
        
        while start + 1 < end:
            mid = (start + end) // 2 

            if nums[mid] <= nums[end]:
                end = mid
            else:
                start = mid 
        
        return min(nums[start], nums[end])
if __name__ == '__main__':
    ll = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    x = ll.findMin(nums)
    print(x)


