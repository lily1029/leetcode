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
        for i in range(k, len(nums)):
            subset.append(nums[i])

            # 这里进行下一层搜索
            self.dfs(nums, i + 1, subset, res)
            
            # 回溯
            del subset[-1]
if __name__ == '__main__':
    ll = Solution()
    nums = [1,2] 
    x = ll.subsets(nums)
    print(x)