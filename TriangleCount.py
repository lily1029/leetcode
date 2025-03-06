class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # we need to sort list S first
        S.sort()
        
        # a global variable to count how many 
        # triangles
        ans = 0

        # go through c in list, takes O(n)
        #这里相当于把i放到最右边，看i左边的两数之和是不是大于i的边
        for i in range(len(S)):
            #set two pointers 
            left, right = 0, i - 1

            while left < right:
                #这里如果两边之和大于第三边
                if S[left] + S[right] > S[i]:
                    # if satisfies above condition, 
                    # there are those number triangeles available 
                    #这里可以算有几个有效的三角形 
                    ans += right - left
                    right -= 1
                else:
                    #这里是两数之和小于第三边，不能构成三角形，left指针往大移
                    left += 1
        return ans
if __name__ == '__main__':
    ll = Solution()
    S = [3, 4, 6, 7]
    x = ll.triangleCount(S)
    print(x)
    