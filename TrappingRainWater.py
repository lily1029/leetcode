class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        if not heights:
            return 0 
        
        # 此题用2个指针，left 和 right, left指向最左边，
        # right 指向最右边
        left, right = 0, len(heights) - 1

        #用left_max 和 right_max 去track 左右两边最高水位线
        #最开始等于左右两边初始值
        left_max, right_max = heights[left], heights[right]

        #这里算多少水
        water = 0

        #go through 整个数组，只要左指针小于等于右指针，直到相交
        #错开后，停止
        while left <= right:
            #当左边最高水位低于右边最高水位
            if left_max < right_max:
                #更新最高水位线在不断向右走的左指针会有更高的值
                left_max = max(left_max, heights[left])
                #当左边最高水位线高于左指针指的水位线，相减，算水量
                #水的多少取决于低位置的量
                water += left_max - heights[left]
                #算出水量后，左指针向右走一步
                left += 1 

            else:
                #这里是left_max >= right_max时的情况
                #更新最大的right_max的值，右指针也在不断变化
                right_max = max(right_max, heights[right])
                #算积水量
                water += right_max - heights[right]
                #算完后，右指针向左， -1 步
                right -= 1 
        #返回最终水的结果
        return water
if __name__ == '__main__':
    ll = Solution()
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]

    x = ll.trapRainWater(heights)
    print(x)
    

