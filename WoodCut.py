class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if not L:
            return 0

        #确定1到max(L)之间进行二分
        start, end = 1, max(L)
        
        while start + 1 < end:
            mid = (start + end) // 2 
            
            #如果此条件 >= k 成立，说明单根木头长度可以在调大一点/长
            #所以扔掉start左半部分，让start = mid值，之后变大mid值
            if self.get_pieces(L, mid) >= k:
                start = mid 
            else:
                #否则，切不出k个木头，单根木头长度要调短，end将值=mid
                #扔掉mid右边大的值， 将end值变小成mid值
                end = mid 
        
        #最后，就剩start, end 两个值，看哪个符合条件就return 哪个
        if self.get_pieces(L, end) >= k:
            return end
        if self.get_pieces(L, start) >= k:
            return start
        return 0 
        
    #验证函数，对于固定长度去for循环
    def get_pieces(self, L, length):
        pieces = 0

        for l in L:
            #得到几根木头就是多少pieces
            pieces += l // length
        return pieces
        
if __name__ =='__main__':
    ll = Solution()
    L = [232, 124, 456]
    k = 7
    x = ll.woodCut(L, k)
    print(x)



