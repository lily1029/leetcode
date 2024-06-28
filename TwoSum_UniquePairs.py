class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        if not nums:
            return 0 
        
        nums.sort()
        
        count = 0 
        l, r = 0, len(nums) - 1 
        
        while l < r:
            value = nums[l] + nums[r]
            if value == target:
                count, l, r = count + 1, l + 1, r - 1 
                while l < r and nums[l] == nums[l - 1]:
                    l += 1 
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1 
            elif value < target:
                l += 1 
            else: 
                r -= 1 
        return count
if __name__ == '__main__':
    ll = Solution()
    nums = [1,1,2,45,46,46]
    target = 47
    x = ll.twoSum6(nums, target)
    print(x)
    