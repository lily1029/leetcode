class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    此题的做法是先把这个数的左边的数先做完乘法，然后在做这个数的右边的数的乘积，除了自己
    """
    def productExceptSelf(self, nums):

        length = len(nums)
        result = [1] * length
        left = 1
        right = 1
        
        # 将第 i 个位置乘上前 i - 1 个数的积
        for i in range(length):

            # 这里的left 是前面数的乘积
            result[i] *= left 
            #这一步在把left *当前的数更新left
            left *= nums[i] 
        
        # 将第 i 个位置乘上后面数的积
        for i in range(length - 1, -1, -1):

            # 这里的right 是后面数的乘积
            result[i] *= right
            #这一步在把right * 后面的数更新right
            right *= nums[i] 
        
        return result
if __name__ == '__main__':
    ll = Solution()
    nums = [2, 3, 8]
    x = ll.productExceptSelf(nums)
    print(x)
