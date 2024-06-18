class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def lastPosition(self, A, target):
        if not A:
            return -1

        start, end = 0, len(A) - 1

        while start + 1 < end:

            mid = (start + end) // 2

            if A[mid] < target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid

        if A[end] == target:
            return end
        if A[start] == target:
            return start
        return -1
if __name__ =='__main__':
    ll = Solution()
    nums = [1, 2, 2, 4, 5, 5]
    target = 2
    x = ll.lastPosition(nums, target)
    print(x)