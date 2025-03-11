class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1 

        while start <= end:
            #odd
            while start <= end and nums[start] % 2 == 1:
                start += 1 
            #even
            while start <= end and nums[end] % 2 == 0:
                end -= 1 
            #exchange
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                #两支针向中间走
                start += 1 
                end -= 1
        
        return nums

if __name__ == '__main__':
    ll = Solution()
    nums = [1, 2, 3, 4]
    x = ll.partitionArray(nums)
    print(x)




