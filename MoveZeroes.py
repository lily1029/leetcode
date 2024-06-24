class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        left, right = 0, 0
        
        while right < len(nums):
            if nums[right] != 0:
                if left != right:
                    nums[left] = nums[right]
                
                left += 1 
            
            right += 1 
        
        while left < len(nums):
            if nums[left] != 0:
                nums[left] = 0 
            left += 1 
        
        return nums
if __name__ == '__main__':
    ll = Solution()
    nums = [0, 1, 0, 3, 12]
    ll.moveZeroes(nums)
    print(nums)

