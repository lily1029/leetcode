import sys
class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # 首先sort（）了input data
        nums.sort()

        #i，j 为左右指针
        i, j = 0, len(nums) - 1

        #global variable to track the minimum difference 
        diff = sys.maxsize 

        #当i < j 时，循环input data 
        while i < j:
            #如果两数之和小于target, 算出这两数之和和target的差，放入diff里，找最小的
            if nums[i] + nums[j] < target:
                diff = min(diff, target - nums[i] -nums[j])
                #左指针+1，找更接近的
                i += 1 
            else:
                #如果两数之和大于target,继续算这两数之和和target的差，继续找最小的diff
                diff = min(diff, nums[i] + nums[j] - target)
                #右指针继续往左移，看有没有更接近target的和找更小
                j -= 1 
        
        #返回closest值to target
        return diff

if __name__ == '__main__':
    ll = Solution()
    nums = [-1, 2, 1, -4]
    target = 4
    x = ll.twoSumClosest(nums, target)
    print(x)
