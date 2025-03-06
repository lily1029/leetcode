class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        #first sort numbers
        numbers.sort()
        
        #最终的结果，初始值为none
        ans = None 
        
        # go through the whole list
        for i in range(len(numbers)):
            # for the rest, we use two pointers
            left, right = i + 1, len(numbers) - 1 

            while left < right:
                # a global variable ans and update it the smallest to ans
                sum = numbers[left] + numbers[right] + numbers[i]
                
                #这里在最开始的时候如果ans是none, ans = 最开始算的sum,
                #在接下来的循环中有新的sum.看新的sum-target 是不是小于已有的ans-target,
                #如果是，更新ans到新的更小的sum为结果
                if ans is None or abs(sum - target) < abs(ans - target):
                    
                    ans = sum 
                
                #two pointer method
                if sum <= target:
                    left += 1 
                else:
                    right -= 1
                     
        return ans

if __name__ == '__main__':
    ll = Solution()
    numbers = [2,7,11,15]
    target = 3
    x = ll.threeSumClosest(numbers, target)
    print(x)