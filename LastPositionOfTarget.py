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

            #这里只需要用<=号，就可以算出last position of the target
            if A[mid] <= target:
                start = mid
            else:
                end = mid

        #因为最后的start 和end 很可能是一样的，因为要求last position,
        #所以这里要先写 if A[end] == target， 然后在 A[start] == target
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



