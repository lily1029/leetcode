# 首先求出nums的前缀和数组 然后将前缀和数组扫一遍，
# 每扫到一个位置就将答案加上前面(k-prefixSum)出现次数（出现次数可以用dict维护） 
# 再将当前前缀和prefixSum在出现的次数+1

class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        # Calculate prefix sum 算前缀和
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
         
        # Initialize dictionary and ans
        d, ans = {0: 1}, 0
        
        # Iterate over prefix sum array, for循环前缀和数组
        #we finally get d: {0: 1, 1: 1, 2: 1, 3: 1}, we have sum is 0, we have 1, sum is 1, we have 1 
        for i in range(len(nums)):
            # If this condition is true, it means there is a valid subarray, accumulate the count in ans
            # #如果此条件成立，说明有合法区间，累计个数在ans里
            if d.get(nums[i] - k) is not None:
                ans += d[nums[i] - k]
            # If not in dictionary, put it in, if exists, increment by 1
            # 如果不在dictionary 里，放入， 如果有，累计加1
            if d.get(nums[i]) is None:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        return ans

# Test Data: 
# [1, 2, 0, 2, 1]
# 3

if __name__ == '__main__':
    ll = Solution()
    nums = [1, 1, 1]
    k = 2
    x = ll.subarraySumEqualsK(nums, k)
    print(x)
