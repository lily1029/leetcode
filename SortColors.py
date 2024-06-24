class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        left, index, right = 0, 0, len(nums) - 1 
        while index <= right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1 
                index += 1
            elif nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1 
            else:
                index += 1
if __name__ == '__main__':
    ll = Solution()
    nums = [1, 0, 1, 2]
    x = ll.sortColors(nums)
    print(nums)
