class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        #用counter 哈希表来存每个数字出现了几次
        counter = {}
        #遍历数组nums并记录每个数字出现的次数
        #test data: nums = [1, 2, 2, 1, 3, 4, 4, 5, 6] number = 5
        #counter: {1:2, 2:2, 3:1, 4:2, 5:1}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            #如果碰到number就停下，只要number之前的数
            if num == number:
                break
        else:
            #如果给的数没有在Data Stream中出来，就返回-1
            #比如example 2 中的 7
            return -1
        
        #在遍历一遍数组，找到出现一次的数字，并返回 
        #nums = [1, 2, 2, 1, 3, 4, 4, 5, 6]  
        for num in nums:
            #counter: {1:2, 2:2, 3:1, 4:2, 5:1}
            #counter[3] == 1, 并且出现在5之前，返回3
            if counter[num] == 1:
                return num
            if num == number:
                break

        return -1
if __name__ == '__main__':
    ll = Solution()

    nums = [1, 2, 2, 1, 3, 4, 4, 5, 6]
    number = 5
    x = ll.firstUniqueNumber(nums, number)
    print(x)



