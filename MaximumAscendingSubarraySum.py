class Solution:
    def maxAscendingSum(self, nums) -> int:

            # max_sum：是求的最终结果，curr_sum：每一个连续上升的subary的sum
            # last_elem：是每个sub array 中的最后一个数（element), 最初都设置为： 0
            max_sum, curr_sum, last_elem = 0, 0, 0

            # go through the nums
            for num in nums:
                #比较当下的num是不是比前一个大，看是不是上升序列 sub array
                if num > last_elem:
                    #如果是上升序列，求sum of sub array
                    curr_sum += num
                else:
                    #如果不是上升序列，说明是另一个sub array 开始
                    #设置curr_sum = 当下的num，开始计算新的sub array
                    curr_sum = num

                #每次go through 完一个num后，更新last_elem为当前的num
                #为了下面继续做比较准备看是不是上升或事下降的 sub array
                last_elem = num
                
                #更新全局变量max_sum 和新得到的sub array 的new sum (curr_sum)
                max_sum = max(max_sum, curr_sum)

            #返回最终结果
            return max_sum

if __name__ == '__main__':
    # Example usage:
    ll = Solution()
    nums = [10,20,30,5,10,50]
    x = ll.maxAscendingSum(nums)
    print(x)
            