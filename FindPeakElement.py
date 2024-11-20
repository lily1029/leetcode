from typing import (
    List,
)

class Solution:
    """
    做这道题主要是要找到peak的点，首和尾都不在peak，所以
    start=1, end=len(a)-2,最主要找到的peak是符合这个
    条件：a[mid] < a[mid + 1]，如果此条件符合，就找到了
    peak 点 
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