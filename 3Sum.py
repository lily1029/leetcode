class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, nums):
        # write your code here
        nums.sort()
        length = len(nums)
        results = []

        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.find_two_numbers(nums, i + 1, length - 1, -nums[i], results)
        return results

    def find_two_numbers(self, nums, left, right, target, results):
        while left < right:
            if nums[left] + nums[right] == target:
                results.append([-target, nums[left], nums[right]])
                right -= 1 
                left += 1 
                while left < right and nums[left] == nums[left - 1]:
                    left += 1 
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1 
            elif nums[left] + nums[right] < target:
                left += 1 
            # elif nums[left] + nums[right] > target:
            else:
                right -= 1
if __name__ == '__main__':
    ll = Solution()
    # nums = [-1,0,1,2,-1,-4]
    nums = [-1,0,1]
    x = ll.threeSum(nums)
    print(x)
    