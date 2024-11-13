from typing import List

class Solution:
    """
    @param a: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    #此题的做法就是二分找到小于target的最大值和大于target的最小值，然后用2个背向双指针看哪个
    #数离target最近，要想做好此题，要分三个模块
    #模块1
    def k_closest_numbers(self, a: List[int], target: int, k: int) -> List[int]:
        #找到A[left] < target, A[right] >= target,也就是最接近target的两个数，他们肯定是邻居
        #所以，找到right后，left = right - 1, 
        #.find_upper_closest()此函数是找到大于target的最小数，此函数就是经典binary search
        right = self.find_upper_closest(a, target)
        left = right - 1
    
        # Two pointers from the middle to both sides to find the k closest numbers
        #找到分开的左右部分后，用两根指针从中间往两边扩展，依次找到最接近的k个数
        results = []#这里放结果
        for _ in range(k):#找k个数
            #如果左边的数更接近target,就把左边的数加进来，left--
            if self.is_left_closer(a, target, left, right):
                results.append(a[left])
                left -= 1
            else:
                #如果右边的数更接近target, 就把右边的数加进来，right++
                results.append(a[right])
                right += 1
        
        return results
    
    #classic binary search here:
    #模块2
    def find_upper_closest(self, a: List[int], target: int) -> int:
        # find the first number >= target in A
        start, end = 0, len(a) - 1
        while start + 1 < end:
            mid = (start + end) // 2

            if a[mid] <= target:
                start = mid
            else:
                end = mid
        
        #因为要找最接近target的最小值，而不是target, 所以这里要用>=target
        if a[start] >= target:
            return start
        
        if a[end] >= target:            
            return end
        
        # If not found
        return end + 1

    #这里看被左右分开的地方，谁的值里target更接近   
    #模块3
    def is_left_closer(self, a: List[int], target: int, left: int, right: int) -> bool:
        if left < 0:
            return False
        if right >= len(a):
            return True
        #这里判断左边的值是不是小于右边，如果是返回true,否则返回false
        return target - a[left] <= a[right] - target

if __name__ == '__main__':
    ll = Solution()
    a = [1, 2, 3]
    target = 2
    k = 3
    # Call k_closest_numbers instead of find_upper_closest
    x = ll.k_closest_numbers(a, target, k)
    print(x)
