from typing import List

class Solution:
    """
    @param a: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def k_closest_numbers(self, a: List[int], target: int, k: int) -> List[int]:
        # write your code here
        right = self.find_upper_closest(a, target)
        left = right - 1
    
        # Two pointers from the middle to both sides to find the k closest numbers
        results = []
        for _ in range(k):
            if self.is_left_closer(a, target, left, right):
                results.append(a[left])
                left -= 1
            else:
                results.append(a[right])
                right += 1
        
        return results
    
    def find_upper_closest(self, a: List[int], target: int) -> int:
        # find the first number >= target in A
        start, end = 0, len(a) - 1
        while start + 1 < end:
            mid = (start + end) // 2

            if a[mid] < target:
                start = mid
            else:
                end = mid
        
        if a[start] >= target:
            return start
        
        if a[end] >= target:            
            return end
        
        # If not found
        return end + 1
        
    def is_left_closer(self, a: List[int], target: int, left: int, right: int) -> bool:
        if left < 0:
            return False
        if right >= len(a):
            return True
        return target - a[left] <= a[right] - target

if __name__ == '__main__':
    ll = Solution()
    a = [1, 2, 3]
    target = 2
    k = 3
    # Call k_closest_numbers instead of find_upper_closest
    x = ll.k_closest_numbers(a, target, k)
    print(x)
