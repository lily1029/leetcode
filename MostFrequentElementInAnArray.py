class Solution:
    def findMostFrequent(self, nums):
        #here we use a hash map to track 
        #how many times each element apear
        countMap = {}
        #here we count the most appear elements
        maxCount = 0
        #here we track the most frequent element
        mostFrequent = None

        #go through the array and use hash to count
        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1 

            #here we compare the current frequent element 
            #number with the maxCount
            if countMap[num] > maxCount:
                #if above is correct, we update maxCount
                maxCount = countMap[num]
                #get the most frequent element
                mostFrequent = num
        return mostFrequent
if __name__ == '__main__':
    ll = Solution()
    nums = [1, 2, 3, 3]
    x = ll.findMostFrequent(nums)
    print(x)
