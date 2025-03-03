class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
    
        #用hash记录{2: 0, 7: 1, 11: 2, 15: 3}
        hash = {}

        #这里i 是它的index， num 是真实的数,在数组里
        for i, num in enumerate(numbers):

            #如果 target 减去 num 在hash里，说明我们找到了这2个数
            #然后返回：这2个数的index  
            if target - num in hash:
                return [hash[target - num], i]
        
        #将num放入hash 里， 并对应它的index 
            hash[num] = i
if __name__ == '__main__':
    ll = Solution()
    numbers = [2, 7, 11, 15]
    target = 13
    x = ll.twoSum(numbers, target)
    print(x)