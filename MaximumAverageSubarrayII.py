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
        start, end = min(nums), max(nums)
        
        while end - start > 1e-5:
            mid = (start + end) / 2 
            if self.check(nums, k, mid):
                start = mid 
            else:
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
