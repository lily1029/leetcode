class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    #此题的做法是用两个同向双指针i 和 j 分别指向nums1 和 nums2
    #一个一个进行比较，如果i指针指的数小于j指的数，i+1，如果j指针指的
    #数小于i指针，j+1，当两个指针都停下时，说明是这两个数组重合的部分
    #放入ans中，然后i和j 都+1，走一步，继续重复比较，记住这里跳过之前
    #重复出现一样的数字
    def intersection(self, nums1, nums2):
        # write your code here
        nums1.sort()
        nums2.sort()
        
        # we put intersection elements in ans 
        ans = []
        
        # two pointers for nums1 and nums2
        i, j = 0, 0

        #循环条件是i< nums1的长度，j < nums2的长度
        while i < len(nums1) and j < len(nums2):

            #如果i指的数小于j, i+1
            if nums1[i] < nums2[j]:
                i += 1
            #如果 j指的数小于 i指的数，j+1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                #find the intersection element and we put in ans 
                ans.append(nums1[i])
                #放完之后 i，j 同时向右都 走一步 +1
                i += 1
                j += 1
                #这里去掉之前重复一样的数，继续往右走
                while i < len(nums1) and nums1[i] == nums1[i-1]:
                    i += 1
                while j < len(nums2) and nums2[j] == nums2[j-1]:
                    j += 1
                    
        return ans
if __name__ == '__main__':
    ll = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    x = print(ll.intersection(nums1, nums2))





