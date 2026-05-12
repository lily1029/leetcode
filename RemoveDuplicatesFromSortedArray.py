class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # 当数组为空时，返回0
        if not nums:
            return 0
        
        #用2个指针的办法，left指针指向
        #数组最左边的元素, 因为array 是
        #sorted, 所以，我们只需要用2个
        #指针比较相邻的两个数字，如果
        #左右指针相等，右指针继续向右走，
        #直到找到左右指针所指向的不同的
        #unique number, 然后右指针
        #覆盖左指针指的数字
        left = 0
        
        #go through array, 右指针最开始
        #是左指针的下一个指针
        for i in range(1, len(nums)):
            #当左右指针指的数字不想等时,
            #这时候找到了unique number
            if nums[left] != nums[i]:
                #左指针向右走一步，这样可以
                #覆盖重复的数字
                left += 1
                #拿右指针覆盖左指针的值
                nums[left] = nums[i]

        #最后返回left 指针所指的长度+第一个数字长度 
        return left + 1

if __name__ == '__main__':
    ll = Solution()
    # nums = [1, 1, 2]
    nums = [0,0,1,1,1,2,2,3,3,4]
    x = ll.removeDuplicates(nums)
    print(x)
    

    



