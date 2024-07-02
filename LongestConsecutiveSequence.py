class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # max_len相当于一个全局变量找最大的,
        # table是一个哈希表
        max_len, table = 0, {num: True for num in num}
        
        #从第一个数开始循环数组，如果第一个数lo-1不再数组里，
        #我们就看看这个数lo+1, 看看lo+1这个数在不在数组里，
        #如果在就一直找下去
        for lo in num:
            if lo - 1 not in table:
                hi = lo + 1 
                while hi in table:
                    hi += 1 
                #这里更新全角变量
                max_len = max(max_len, hi - lo)
                
        return max_len
if __name__ =='__main__':
    ll = Solution()
    num = [100, 4, 200, 1, 3, 2]
    x = ll.longestConsecutive(num)
    print(x)