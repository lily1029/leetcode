class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if not nums:
            return -1 
        
        start, end = 0, len(nums) - 1 
        while start + 1 < end:
            mid = (start + end) // 2 
            if nums[mid] >= nums[mid + 1]:
                end = mid 
            else: 
                start = mid 
        
        return max(nums[start], nums[end])
if __name__ == '__main__':
    ll = Solution()
    nums = [1, 2, 4, 8, 6, 3]
    # Call k_closest_numbers instead of find_upper_closest
    x = ll.mountainSequence(nums)
    print(x)