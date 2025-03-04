class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # 如果nums 为空，两数之和直接返回0
        if not nums:
            return 0 
        
        #先把nums sort 一下，在排好序的数组上进行two pointer method
        nums.sort()
        
        #global variable, 看有几个unique pairs
        count = 0 
        #l:最左边，r:最右边
        l, r = 0, len(nums) - 1 
        
        #while 循环 left < right:
        while l < r:
            #先算两数之和
            value = nums[l] + nums[r]
            #先比较两数之和是不是等于target，如果是，count + 1, l,r分别向右和左移一步
            if value == target:
                count, l, r = count + 1, l + 1, r - 1 

                #这里有可能出现重复的pairs, 这里剪掉左边的重复
                while l < r and nums[l] == nums[l - 1]:
                    l += 1 
                #这里剪掉右边的重复
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1 
            #如果两数之和小于target, 左指针向右移一步，变大一点
            elif value < target:
                l += 1 
            else: 
                #否则两数之和大于target, 移动右指针向左一步，变小一点
                r -= 1 
        
        #返回结果
        return count
if __name__ == '__main__':
    ll = Solution()
    nums = [1,1,2,45,46,46]
    target = 47
    x = ll.twoSum6(nums, target)
    print(x)
    



