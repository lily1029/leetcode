import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        #result 里存 merge 后的结果
        result = []
        
        #这里用heap 去sort
        heap = []
        
        #for循环题目给的arrays
        for index, array in enumerate(arrays):

            if len(array) == 0:
                continue
            
            #并将循环的第一个元素用一个三元组推到堆里
            #index是array里的次序，0:是每个小array里的index
            heapq.heappush(heap, (array[0], index, 0))
        
        #当heap的长度不为零时，对它进行循环
        while len(heap):

            #取出heap中的最小值
            val, x, y = heap[0]

            #把这个值pop()出来
            heapq.heappop(heap)

            #并且把这个值放入到result中
            result.append(val)
            
            #如果y + 1 < arrays[x]的长度，说明还有剩下的值要比较
            #在这个array的下一个值是：arrays[x][y+1],同时我们要保持
            #行坐标和列坐标+1 
            if y + 1 < len(arrays[x]):
                heapq.heappush(heap, (arrays[x][y + 1], x, y + 1))

        return result
if __name__ == '__main__':
    # Example usage:
    ll = Solution()
    arrays = [[1, 3], [2, 4], [0, 8]]
    x = ll.mergekSortedArrays(arrays)
    print(x)



