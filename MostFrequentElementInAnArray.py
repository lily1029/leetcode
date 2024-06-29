class Solution:
    def findMostFrequent(self, nums):
        countMap = {}
        maxCount = 0
        mostFrequent = None

        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1 

            if countMap[num] > maxCount:
                maxCount = countMap[num]
                mostFrequent = num
        return mostFrequent
if __name__ == '__main__':
    ll = Solution()
    nums = [1, 2, 3, 3]
    x = ll.findMostFrequent(nums)
    print(x)
