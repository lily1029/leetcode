class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        self.sort(colors, 1, k, 0, len(colors) - 1)
    
    #here define a helper method sort()    
    def sort(self, colors, color_from, color_to, index_from, index_to):
        # the corner case when it is only one color, storp and return 
        if color_from == color_to or index_from == index_to:
            return
        
        # here we find a pivot element and do the partition  
        color = (color_from + color_to) // 2
        
        #like quicksort 
        left, right = index_from, index_to
        while left <= right:
            while left <= right and colors[left] <= color:
                left += 1
            while left <= right and colors[right] > color:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
        
        #recursively do the left part, 这时候left和right已经交错了,right到了左边，left到了右边
        #color 也被partition 成 color_from 到pivoit color, 从左边界到right指针
        self.sort(colors, color_from, color, index_from, right)
        # recursively do the right
        #这里被partition 成color + 1 到color_to, 然后用left 指针到最右的边界
        self.sort(colors, color + 1, color_to, left, index_to)

if __name__ == '__main__':
    ll = Solution()
    colors = [3,2,2,1,4] 
    k = 4 
    x = ll.sortColors2(colors, k)
    print(colors)
