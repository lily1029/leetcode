class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # 这里设立三个指针，left, index, right, left左侧都是0
        #right右侧都是2， index从左到右扫描一遍，如果碰见0，就和left交换
        left, index, right = 0, 0, len(nums) - 1 
        while index <= right:
            #index从左到右扫描一遍，如果碰见0，就和left交换
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1 
                index += 1
            #index从左到右扫描一遍，如果碰见2，就和right交换
            elif nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1 
            else:
                #碰到1，跳过去，不管
                index += 1
if __name__ == '__main__':
    ll = Solution()
    nums = [1, 0, 1, 2]
    x = ll.sortColors(nums)
    print(nums)
