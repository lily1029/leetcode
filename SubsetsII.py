class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        #存最终结果
        res = []

        # 排序
        nums.sort()

        # dfs搜索
        self.dfs(nums, 0, [], res)

        #返回最终结果res
        return res
        
    def dfs(self, nums, k, subset, res):
        # 当前组合存入res
        res.append(subset[:])

        # 为subset新增一个元素
        for i in range(k, len(nums)):
            # 剪枝, 如果nums[i] == nums[i - 1]，说明有重复的数字
            # continue 掉后面的代码
            #这里i != k，是因为，i 要for循环k 到 len(nums)长度，i已经到了
            #k的下一个数字
            if (i != k and nums[i] == nums[i - 1]):
                continue

            #这里，当k=i时，表示可以向子集中添加nums[i:]
            subset.append(nums[i])
            #这里是对nums[i]开头的子集，进行下一层搜索
            self.dfs(nums, i + 1, subset, res)
            # 搜索完之后，进行回溯
            del subset[-1]

if __name__ == '__main__':
    ll = Solution()
    nums = [1,2,2]
    x = ll.subsetsWithDup(nums)
    print(x)