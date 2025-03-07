class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        
        # 如果是奇数
        if (m + n) % 2 == 1:
            return self.getKth(A, 0, m - 1, B, 0, n - 1,  (m + n) // 2 + 1)
        
        # 如果是偶数
        left = self.getKth(A, 0, m - 1, B, 0, n - 1,  (m + n) // 2)
        right = self.getKth(A, 0, m - 1, B, 0, n - 1,  (m + n) // 2 + 1)
        return (left + right) / 2 
       
    def getKth(self, A, start1, end1, B, start2, end2, k):
        len1 = end1 - start1 + 1 
        len2 = end2 - start2 + 1 
        
        # 让len1的长度小于len2，这样就能保证如果有数组空了,一定是len1
        # 比如 test case A=[2], B=[]
        if len1 > len2:
            return self.getKth(B, start2, end2, A, start1, end1, k)
        
        # A数组排除完毕, A 和B交换后，直接返回B数组中的数，当A为空的时候
        if len1 == 0:
            return B[start2 + k - 1]
            
     
        # 已经找到第k小的数
        if k == 1:
            return min(A[start1] , B[start2])
       
        # 开始二分
        i = start1 + min(len1, k // 2) - 1 
        j = start2 + min(len2, k // 2) - 1 
        
        #i, j分别为A, B数组的指针，进行比较大小，来决定第几个getKth element
        if A[i] > B[j]:
            return self.getKth(A, start1, end1, B, j + 1, end2, k - (j - start2 + 1))
        else:
            return self.getKth(A, i + 1, end1, B, start2, end2, k - (i - start1 + 1))
if __name__ =='__main__':
    ll = Solution()
    # A = [1,2,3]
    # B = [4,5]
    A = [2]
    B = []
    x = ll.findMedianSortedArrays(A, B)
    print(x)


