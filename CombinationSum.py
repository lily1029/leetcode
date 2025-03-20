class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # 这里sort并去重
        candidates = sorted(list(set(candidates)))
        #存最终结果
        results = []
        #调用dfs
        self.dfs(candidates, target, 0, [], results)
        #返回结果
        return results

    # 递归的定义：在candidates[start ... n-1] 中找到所有的组合，他们的和为 target
    # 和前半部分的 combination 拼起来放到 results 里
    # 找到所有以 combination 开头的满足条件的组合，放到 results
    def dfs(self, candidates, target, start, combination, results):
        # 递归的出口：
        #此题的输入数据全部是正整数，如果出现target < 0, 直接返回 即可
        if target < 0:
            return
        
        #当target 等于0，找到了符合条件的解
        if target == 0:
            # deepcooy
            return results.append(list(combination))
            
        # 递归的拆解：从数组第一个数开始一个个放进去，看是否和为target
        for i in range(start, len(candidates)):
            # [2] => [2,2]
            combination.append(candidates[i])
            #放完一个数后，进行下层dfs, 此时，target变了，搜索的起始位置总是从0开始，直到数组结束
            self.dfs(candidates, target - candidates[i], i, combination, results)
            # [2,2] => [2]
            # backtracking
            #一层搜索完，弹出最后的数，进行下一路径的搜索
            combination.pop()  

if __name__ == '__main__':
    ll = Solution()
    #candidates = [2, 3, 6, 7]
    candidates = [2, 3, 7]
    target = 7
    x = ll.combinationSum(candidates, target)
    print(x)
