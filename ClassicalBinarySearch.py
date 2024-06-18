class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    @the classical binary search is same as First Position of Target in Binary Search
    """
    def findPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2 
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        
        if nums[start] == target:
            return start
        
        if nums[end] == target:
            return end 

        return -1
if __name__ =='__main__':
    ll = Solution()
    nums = [1, 2, 2, 4, 5, 5]
    target = 2
    x = ll.findPosition(nums, target)
    print(x)
