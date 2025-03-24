# 解法：先固定最左边的第一个数， 然后一个一个循环剩下的数
# e.g [1, 2] x
#       [1, 3] x
# 			[1, 4] v
# 	在固定2，然后循环剩下的数一个一个
# 	    [2, 3] v
# 			[2, 4] x
# 	直到最后
# 	   [3. 4] x
# 		 [4] x 
		 
class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # sort A list first 
        A = sorted(A)

        # we define subsets to store final results 
        subsets = []

        #call dfs method,这种求所有解的都用dfs
        self.dfs(A, 0, k, target, [], subsets)

        #返回结果
        return subsets
    
    # dfs starts here ，k是几个数, 求得的和等于target,
    # subset是一个占时存放数字的list
    def dfs(self, A, index, k, target, subset, subsets):
        #递归出口，找到满足条件的答案
        if k == 0 and target == 0:
            subsets.append(list(subset))
            return
        
        #不符合条件的，返回
        if k == 0 or target <= 0:
            return
        
        #递归的拆解，在数组里的数，不可以重复使用,所以用index
        for i in range(index, len(A)):
            #先将这个数放入到subset 里
            subset.append(A[i])
            #然后在剩下的数组里进行dfs,看有没有还有剩下的数可以组成k个数，
            #并且sum 等于target, 
            #由于不可以重复，所以index = i + 1, 是i的下一个
            #每次进行下层搜索， 要更新new target = target - A[i]
            self.dfs(A, i + 1, k - 1, target - A[i], subset, subsets)
            #backtracking
            subset.pop()
if __name__ == '__main__':
    ll = Solution()
    array = [1,2,3,4]
    k = 2
    target = 5
    x = ll.kSumII(array, k, target)
    print(x)