class Solution:    
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    #此题的做法和lintcode135基本一样，只是它的dfs不从i位置开始，从i+1位置开始进行dfs
    def combinationSum2(self, candidates, target): 
        #we sort candidates first
        candidates.sort()  

        #ans用来存结果，tmp 用来暂存放入的数字，use用来做标记数字是否已经放进去
        self.ans, tmp, use = [], [], [0] * len(candidates)   

        #call dfs method 
        self.dfs(candidates, target, 0, 0, tmp, use)   
        
        #返回答案   
        return self.ans  
        
    #can is candidates, start要加数字起点，now：当前数字的和
    def dfs(self, can, target, start, now, tmp, use):   
        #当now相加的数字和等于target时，就找到了解     
        if now == target:            
            self.ans.append(tmp[:])            
            return  

        #递归拆解      
        for i in range(start, len(can)): 
            #这里进行剪枝，如果是相同的数同时出现，要确保前一个以用过（use[i-1]==1)
            #对于不相同的数，可以直接加进去
            #当i=0第一个 数时，直接加进去
            if now + can[i] <= target and (i == 0 or can[i] != can[i-1] or use[i-1] == 1):                
                tmp.append(can[i])
                #放入后做标记
                use[i] = 1  
                #下层dfs, 这里从 i+1 开始              
                self.dfs(can, target, i+1, now + can[i], tmp, use) 
                #当递归完后，pop()出最后的数，并且use 清0               
                tmp.pop()                
                use[i] = 0
if __name__ == '__main__':
    ll = Solution()
    num = [7,1,2,5,1,6,10]
    target = 8

    x = ll.combinationSum2(num, target)
    print(x)


