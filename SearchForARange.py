class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if len(A) == 0:
            return [-1, -1]
        
        start, end = 0, len(A) - 1 
        while start + 1 < end:
            mid = (start + end) // 2 
            # 如过 A[mid] < target, 显然这时查找数值偏小，说明答案在右区间，
            # 因此使 start = mid 来放大查找数值。 
            #找target first position用这个： A[mid] < target:
            if A[mid] < target:
                start = mid
            else:
                end = mid 
        
        # after binary search, we only left two elements either start or end 
        # we continue looking for the leftBound, otherwise return [-1, -1]
        if A[start] == target:
            leftbound = start
        elif A[end] == target:
            leftbound = end 
        else:
            return [-1, -1]
            
        # binary Search for second time to look for the rightbound
        # because we found the leftBound as above, so, the next binary search, we 
        # start from the leftBound
        start, end = leftbound, len(A) - 1 
        while start + 1 < end:
            mid = (start + end) // 2 
            #找target last position用这个： A[mid] <= target:
            if A[mid] <= target:
                start = mid
            else:
                end = mid 
        
        if A[end] == target:
            rightbound = end 
        else:
            rightbound = start
       
        return [leftbound, rightbound]
if __name__ =='__main__':
    ll = Solution()
    array = [5, 7, 7, 8, 8, 10]
    target = 8
    x = ll.searchRange(array, target)
    print(x)