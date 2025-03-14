class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0 
       
        #将初始数据sort()了
        nums.sort()
        
        #这里使用两个同向双指针，result是左指针
        result = 1 
        
        #i相当于是右指针，左右指针在从左往右走时，一前一后，比较2个指针是否一致，
        #如果不一致，用右指针的值覆盖到左指针上，然后左右指针都+1继续往前走，
        #这样使左右指针的值不一样，最后当右指针走完后
        #左指针的位置就是有多少是no duplicate number
        #i指针start 1, 左指针 result start 0
        for i in range(1, len(nums)):

            #当左右指针的值不一样时，右指针的值覆盖左指针的值，左指针+1，
            if nums[i - 1] != nums[i]:
                nums[result] = nums[i]
                result += 1 

        return result

if __name__ =='__main__':
    ll = Solution()
    nums = [1,3,1,4,4,2]
    x = ll.deduplication(nums)
    print(x)