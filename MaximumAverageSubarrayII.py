class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        # write your code here
        if not nums:
            return 0 
        #here the start is the smallest number in nums
        #here end is the largest number in nums
        #here we use the way to binary search the answer
        start, end = min(nums), max(nums)
        
        while end - start > 1e-5:
            mid = (start + end) / 2 
            #检查在数组nums里是否可以找到一个
            #子数组个数等于k，且最大均值是mid，如果可以
            #找到返回true, start = mid, 代表这个最终的值
            #可以在均值mid 的基础上在往上调
            if self.check(nums, k, mid):
                start = mid 
            else:
                #返回false, 代表找不到这样的子数组，均值
                #要往小调
                end = mid 
        return start 
        
    
    def check(self, nums, k, average):
        #这个数组算prefixsum和并且减去了average, 这样我们在原数组中只要找到长度
        #大于等k的子数组和大于等于0就可以，返回True 
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num - average)
        
        #这里的这个minPrefixSum是个全局变量
        minPrefixSum = 0 
        for i in range(k, len(nums) + 1 ):
            #只要找到一个子数组长度大于等于k, 且它的和大于等于0，就是True的
            if prefixSum[i] - minPrefixSum >= 0:
                return True 
            
            minPrefixSum = min(minPrefixSum, prefixSum[i - k + 1])
            
        return False
if __name__ =='__main__':
    ll = Solution()
    nums = [1,12,-5,-6,50,3]
    k = 3
    x = ll.maxAverage(nums, k)
    print(x)
