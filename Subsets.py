class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        #res里存所有的subsets
        res = []

        # 排序
        nums.sort()

        # call dfs搜索
        self.dfs(nums, 0, [], res)
        
        #返回结构
        return res

    #nums题目给的输入，k表示当前子集的长度   
    def dfs(self, nums, k, subset, res):
        # 先把当前组合存入res
        res.append(subset[:])

        # 为subset新增一位元素
        #这里，如果k=i时，表示可以向子集中添加nums[i:]
        #中任何一个元素，此时面临len(nums) - i个选择
        #这里要for 循环len(nums)的长度，因为会有
        #不同的 nums[i]开头的子集，
        for i in range(k, len(nums)):
            
            #这里表示以nums[i]开头的子集
            subset.append(nums[i])

            # 这里是对nums[i]开头的子集，进行下一层搜索
            self.dfs(nums, i + 1, subset, res)

            # 当搜索结束，回溯
            del subset[-1]
if __name__ == '__main__':
    ll = Solution()
    nums = [1,2] 
    x = ll.subsets(nums)
    print(x)