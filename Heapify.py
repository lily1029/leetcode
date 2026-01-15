import heapq
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    
    def siftup(self, A, now):
        #while 这个节点不是空
        #When now == 0, bool(0) is False,so the loop does not run.
        while now:
            #获取它的father节点
            #在binary tree里，如果想获取父亲节点的index值，就是
            #（孩子节点的index值 - 1）// 2
            father = (now-1)//2
            
            #当我当前节点比父亲大,说明父亲节点值小时，我就停下来break
            #因为是min heap, 所以父亲节点大于我，就对了
            if A[now] > A[father]:
                break
            
            #否则当前节点比父亲小，所以当前节点A[now]和父亲节点交换
            #让父亲节点在上面
            A[now], A[father] = A[father], A[now]
            #当now 和father交换后，now也更新为交换后的父亲节点
            now = father
    def heapify(self, A):
        # write your code here
        #for循环go throug array A, 并对每个数siftup
        #如果孩子比父亲大，这里是min heap
        for i in range(len(A)):
            self.siftup(A, i)
        
        return A


if __name__ == '__main__':
    ll = Solution()
    A = [3,2,1,4,5]
    x = ll.heapify(A)
    print(x)
   