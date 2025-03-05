class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """
    def twoSum7(self, nums, target):
        # 先拿到input的长度
        n = len(nums)

        #如果target 小于0， 找-target
        if target < 0:
            target = - target

        #这里i, 和 j 是2个同向双指针，j在i的前面    
        j = 0 
        #for 循环 input data 长度
        for i in range(n):
            #如果i, 和 j指向同一个地方，j+1 挪到前面去
            if j == i:
                j += 1 
            
            #在j<n的情况下循环， 如果两数之差小于target, 移动j指针
            while j < n and nums[j] - nums[i] < target:
                j += 1 
            
            #如果两数之差等于target, 返回这两个数
            if j < n and nums[j] - nums[i] == target:
                return [nums[i], nums[j]]

if __name__ == '__main__':
    ll = Solution()
    nums = [2, 7, 15, 24]
    target = 5 
    x = ll.twoSum7(nums, target)
    print(x)

