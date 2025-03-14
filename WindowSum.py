class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        n = len(nums)

        # 如果给的值都 小于要加的k个数，直接返回空[]
        if n < k or k <= 0:
            return []
            
        # 这里初始一个new list,值全为0，算滑动窗口k个数的和
        sums = [0] * (n - k + 1)
        
        # 这里算出在sum里第一个k个数的和
        for i in range(k):
            sums[0] += nums[i];
        
        # 这里开始滑动窗口从位置1往右滑，一直滑倒窗口右边界
        #右边界值为n-k+1
        for i in range(1, n - k + 1):
            #这里用前一个窗口的和，减去前窗口最左边的一个数，
            #并且加上新窗口最右边的一个数，成为一个新窗口的和值
            #前一窗口的和是： sums[i - 1] 
            #前一窗口最左边的数是：nums[i - 1]
            #新窗口最右边的数是：nums[i + k - 1]
            sums[i] = sums[i - 1] - nums[i - 1] + nums[i + k - 1]

        #最后返回新的窗口和的集合
        return sums
if __name__ =='__main__':
    ll = Solution()
    nums = [1,2,7,8,5]
    k = 3
    x = ll.winSum(nums, k)
    print(x)
