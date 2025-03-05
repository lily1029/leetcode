class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, nums):
        #first sort nums
        nums.sort()
        
        #use results to store final results
        results = []

        #get length of list nums
        length = len(nums)

        # here is length - 2 because it is 3 sums
        # here we start to go through a in the list
        for i in range(0, length - 2):
        # 这里去掉a中重复相等的
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            #在剩下的list里找两数之和等于 -nums[i]
            self.find_two_sum(nums, i + 1, length - 1, -nums[i], results)
        return results

    # here is 2Sum 
    def find_two_sum(self, nums, left, right, target, results):
        
        while left < right:

            if nums[left] + nums[right] == target:
                results.append([-target, nums[left], nums[right]])
                right -= 1
                left += 1

                #去掉重复的b
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                #去掉重复的c
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif nums[left] + nums[right] < target:
                left += 1 
            else:
                right -= 1 
            
if __name__ == '__main__':
    ll = Solution()
    nums = [-1,0,1,2,-1,-4]
    #nums = [-1,0,1]
    x = ll.threeSum(nums)
    print(x)
    