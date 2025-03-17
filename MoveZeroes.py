class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    #此题的做法是用两个同向双指针做，left, right两个指针从左
    #往右滑完整个nums, 右指针走的更快，当右指针碰到不是0的数字
    #用右指针的值覆盖左指针的值，当然要比较左右指针不在同一个地方，要不然
    #白覆盖。当右指针把所有非0的数都覆盖到左指针指的位置后，然后左指针负责把
    #剩下的数字全部覆盖成0，结束。
    def moveZeroes(self, nums):
        #左右指针初始化
        left, right = 0, 0
        
        #当右指针小于整个nums的长度时，开始
        while right < len(nums):
            #如果右指针指的数不是0，查看如果left != right 进行覆盖
            if nums[right] != 0:
                if left != right:
                    nums[left] = nums[right]
                
                #覆盖完后 左指针 + 1，  走一步
                left += 1 
            
            #右指针也 + 1， 走一步
            right += 1 
        
        #这里归0剩下的数，当左指针小于整个数组长度
        while left < len(nums):
            #如果左指针指的不是0， 覆盖成0
            if nums[left] != 0:
                nums[left] = 0 
            #左指针向前走一步， 直到走完整个数组
            left += 1 
        
        #返回新的数组
        return nums
if __name__ == '__main__':
    ll = Solution()
    nums = [0, 0, 0, 3, 1]
    ll.moveZeroes(nums)
    print(nums)




