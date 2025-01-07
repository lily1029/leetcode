class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        if not A:
            return 0

         #寻找第一次出现的位置
        start, end  = 0, len(A) - 1

        while  start + 1 < end:
            
            mid = ( start + end) // 2

            if A[mid] < target:

                start = mid

            else:

                end = mid
       

        if A[start] == target:

            first = start

        elif A[end] == target:

            first = end 

        #若找不到直接返回0

        else:

            return 0

        
        #寻找最后一次出现的位置

        start, end  = first, len(A) - 1

        while start + 1 < end:
            
            mid = (start + end) // 2 

            if A[mid] <= target:

                start = mid

            else:

                end = mid

        
        #注意与first的判断顺序有别，要先判右侧的

        if A[end] == target:

            last = end

        elif A[start] == target:

            last = start
                        
        return last - first + 1
if __name__ =='__main__':
    ll = Solution()
    A = [1, 3, 3, 4, 5]
    target = 3
    x = ll.totalOccurrence(A, target)
    print(x)

