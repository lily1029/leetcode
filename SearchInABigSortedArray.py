class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        start, end = 0, 1 
        
        while  reader.get(end) <= target:
            end = 2 * end 
      
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
if __name__ =='__main__':
    ll = Solution()
    reader = [1, 3, 6, 9, 21, ...]
    target = 3
    x = ll.searchBigSortedArray(reader, target)
    print(x)