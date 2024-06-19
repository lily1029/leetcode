from typing import (
    List,
)

class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """
    def find_peak(self, a: List[int]) -> int:
        # write your code here
        start, end = 1, len(a) - 2

        while start + 1 < end:
            mid = (start + end) // 2 
            if a[mid] < a[mid + 1]:
                start = mid 
            else:
                end = mid 
        
        if a[end] > a[start]:
            return end
        else:
            return start
if __name__ == '__main__':
    ll = Solution()
    a = [1,2,3,4,1]
    x = ll.find_peak(a)
    print(x)