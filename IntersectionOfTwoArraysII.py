class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        nums1.sort()
        nums2.sort()
        
        ans, i, j = [], 0, 0 
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1 
            elif nums1[i] > nums2[j]:
                j += 1 
            else:
                ans.append(nums1[i])
                i += 1 
                j += 1 
        return ans
if __name__ == '__main__':
    ll = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    x = print(ll.intersection(nums1, nums2))





