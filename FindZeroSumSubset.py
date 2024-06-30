class Solution:

    def find_zero_sum_subset(self, nums):
        def backtrack(start, path):
            if sum(path) == 0 and path:
                return path
            for i in range(start, len(nums)):
                result = backtrack(i + 1, path + [nums[i]])
                if result:
                    return result
            return []

        return backtrack(0, [])

if __name__ == '__main__':
    ll = Solution()
    nums = [1, -1, 2, -2]
    x = ll.find_zero_sum_subset(nums)
    print(x)

