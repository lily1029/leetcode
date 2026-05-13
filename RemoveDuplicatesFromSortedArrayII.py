class Solution:
    def removeDuplicates(self, nums):
        # 获取数组长度
        n = len(nums)
        # 如果数组长度<=2，直接返回（不可能有超过2个重复）
        if n <= 2:
            return n
        
        # 双指针都从索引2开始（前两个元素默认保留）
        slow, fast = 2, 2

        # fast指针遍历整个数组
        while fast < n:
            #如果当前nums[fast]的数 与 slow指针往前数2个数指的数不同
            #说明nums[fast]出现次数未超过2次，可以保留, 如果相等表示
            #一个数已经出现超过2次，此时移动右指针，准备覆盖
            if nums[slow - 2] != nums[fast]:
                # 将fast指向的元素写入slow位置
                nums[slow] = nums[fast]
                # slow指针前进
                slow += 1
            # fast指针每轮必须前进
            fast += 1

        # slow就是最终有效元素的个数k
        return slow

if __name__ == '__main__':
    ll = Solution()
    nums = [1,1,1,2,2,3]
    x = ll.removeDuplicates(nums)
    print(x)
    

    



