class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # 先sort()了nums里的数
        nums.sort()
        #最后满足题目的结果几个
        res = 0 
        
        #左右指针
        l, r = 0, len(nums) - 1 
        #当l<r时进行循环
        while l < r:
            #如果两指针和小于等于target,不符合，左指针+1向右走
            if nums[l] + nums[r] <= target:
                l += 1 
            else:
                #两数和大于target,这时，r-l算个数
                res += r - l 
                r -= 1 
        
        return res
if __name__ == '__main__':
    ll = Solution()
    nums = [2, 7, 11, 12, 13, 15] 
    target = 24
    x = ll.twoSum2(nums, target)
    print(x)
