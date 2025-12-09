class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # left, riht 分别为左右指针
        left, right = 0, len(nums) - 1 

        #如果left < right 做循环
        while left < right:
            #查看两数之和
            value = nums[left] + nums[right]

            #如果两数之和等于target, 返回 index, 因为是index从1开始 
            #所以 left + 1, right + 1
            if value == target:
                return [left + 1, right + 1]
            #如果两数之和小于target, left往大移一步， 否则右指针向左移
            elif value < target:
                left += 1 
            else:
                right -= 1 
        return []

if __name__ == '__main__':
    ll = Solution()
    nums = [2, 7, 11, 15]
    target = 9 
    x = ll.twoSum(nums, target)
    print(x)

   