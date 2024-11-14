class ArrayReader:
    def __init__(self, array):
        self.array = array

    def get(self, index):
        if index >= len(self.array):
            return float('inf')  # Simulate an out-of-bounds access with a large value
        return self.array[index]

class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        #因为我们不知道array的长度，所以，最开始start = 0, end = 1, 去设定最小的array的左右边界
        start, end = 0, 1
        
        # Expand the search range exponentially until the end is greater than the target
        while reader.get(end) < target:
            end = 2 * end
        
        # Perform binary search within the determined range
        while start + 1 < end:
            mid = (start + end) // 2
            if reader.get(mid) < target:
                start = mid
            else:
                end = mid
        
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1

if __name__ == '__main__':
    ll = Solution()
    reader = ArrayReader([1, 3, 6, 9, 21])
    target = 9
    x = ll.searchBigSortedArray(reader, target)
    print(x)  # Output should be 1


