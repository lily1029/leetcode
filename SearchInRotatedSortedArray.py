class Solution:
    """
    这道题的做法就是：因为它是rotated sorted array,这个array就分成了2
    部分，上面一部分，下面一部分，所以分界线条件是 A[mid] >= A[start]在
    上部分，否则就是分在了下部分，详情请看图
    """

    def search(self, A, target):
        if not A:
            return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # here is the left upper case
            if A[mid] >= A[start]:
                if A[start] <= target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                # this case is right bottom 
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid
         # here is we have limited only two elements left
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
if __name__ == '__main__':
    ll = Solution()
    A = [4, 5, 1, 2, 3]
    target = 1
    x = ll.search(A, target)
    print(x)


