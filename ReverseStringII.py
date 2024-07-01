class Solution:
    """
    @param s: the string
    @param k: the integer k
    @return: the answer
    """
    def reverseStringII(self, s, k):
        ls = list(s)   # 变成list
        left, right = 0, len(ls) - 1 
        
        #go through the list, each time skip 2*k number
        for i in range(0, len(ls), 2 * k):
            #slist[i:i+k] = reversed(slist[i:i+k])   # 用库的话这一步就解决了
            #fint left pointer
            left = i
            #here we find right pointer
            right = min(i + k - 1, len(s) - 1)
            
            #here we reverse
            while left < right:
                ls[left], ls[right] = ls[right], ls[left]
                #here we move left and right pointers
                left += 1 
                right -= 1 
        
        return "".join(ls)   #再变回来
if __name__ == '__main__':
    ll = Solution()
    s = "abcdef"
    k = 2
    x = ll.reverseStringII(s, k)
    print(x)
