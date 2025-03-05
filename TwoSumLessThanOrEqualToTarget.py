class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def two_sum5(self, nums, target):
        
        # first we sort nums
        nums.sort()
        # use two pointers at begining and end
        l, r = 0, len(nums)-1
        # a global variable to count how many in total
        cnt = 0

        while l < r:
            # figure out left and right sum value
            value = nums[l] + nums[r]
            #这里让两数之和和target进行比较，如果大于target, 
            #移动右指针向左一步
            if value > target:
                r -= 1
            else:
                #这里满足两数之和小于target，因为是sort array,
                #所以用r-l可以直接算出l 加 r-l 个都满足，然后左指针
                #向右走一步，变大一步，继续查找更大的两数之和是不是满足条件
                cnt += r - l
                l += 1
        return cnt
if __name__ == '__main__':
    ll = Solution()
    nums = [2, 7, 11, 15]
    target = 24
    x = ll.two_sum5(nums, target)
    print(x)

