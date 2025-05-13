import heapq

class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        # 得到matrix的行数
        n = len(matrix)

        # 如果行数为0，返回None
        if n == 0:
            return None
        
        # 得到matrix的列数
        m = len(matrix[0])

        # 如果列为0，返回None
        if m == 0:
            return None
        
        # 初始化一个minheap,最小的数一定是matrix[0][0],这里放了一个三
        # 元祖，（num, num的横坐标，num的纵坐标）
        minheap = [(matrix[0][0], 0, 0)]

        # 把第一个放入minheap的数标记在visited的set中
        visited = set([0])

        # 要求得的第k大的数(num)，初始值为None               
        num = None

        #这里for循环k次, 找到第k大的数
        for _ in range(k):

            #弹出minheap中的最小的数，和这个数所在的横纵坐标
            num, x, y = heapq.heappop(minheap)

            #判断是否越界，并给这个点算一个标记点放入set中
            if x + 1 < n and (x + 1) * m + y not in visited:

                #将这个点的下一行点推入minheap
                heapq.heappush(minheap, (matrix[x + 1][y], x + 1, y))
                
                #标记此点在set中，以免重复放入heap中
                visited.add((x + 1) * m + y)
            
            #在看这个点右边的点，是否越界，并给这个点算一个标记点放入set中
            if y + 1 < m and x * m + y + 1 not in visited:

                #将这个点的右边，也就是下一列的点推入minheap
                heapq.heappush(minheap, (matrix[x][y + 1], x, y + 1))

                #标记此点在set中，以免重复放入heap中
                visited.add(x * m + y + 1)

        #上面K次for循环结束后，弹出的这个num就是第k个number
        return num

if __name__ =='__main__':
    ll = Solution()

    matrix = [
                [1 ,5 ,7],
                [3 ,7 ,8],
                [4 ,8 ,9],
                ]

    k = 4

    x = ll.kthSmallest(matrix, k)
    print(x)
    


