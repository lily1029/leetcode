class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1 
        
        while start < end:
            mid = (start + end) // 2 
            
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid + 1
            else:              
                end -= 1 
            
        return nums[start]
if __name__ == '__main__':
    ll = Solution()
    nums = [4, 4, 5, 6, 7, 0, 1, 2]
    x = ll.findMin(nums)
    print(x)


