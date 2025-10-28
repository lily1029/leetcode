class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        #先把heaters sort 一下
        heaters.sort()
        #这里是要算的radius
        ans = 0
        
        # go through 整个houses, 找到所有houses离它们最近的heaters的最大值
        for house in houses:
            ans = max(ans, self.closestHeater(house, heaters))
        return ans 
    
    #此函数是找离一个房子最近的heater的最小值
    def closestHeater(self, house, heaters):
        start, end = 0, len(heaters) - 1 

        #这里是二分heaters这个数组，找到中间的heater,然后看这个heater离这个房子的远近，
        #在看是去用左边的heater 还是用右边的heater
        while start + 1 < end:
            #找中间的heater位置，进行二分比较
            mid = (start + end) // 2 
            #如果heater 和房子重合，返回0
            if heaters[mid] == house:
                return 0
            #如果heater的距离大于house的距离，说明heater完全可以加热到这个房子，设置成end,
            #在和前一个heater进行下比较，谁离这个房子比较近
            elif heaters[mid] > house:
                end = mid   
            else:
                start = mid 
        
        #这里返回start heater 和 end heater 距离这个房子的最小值
        return min(abs(house - heaters[start]), abs(house - heaters[end]))
    
if __name__ =='__main__':
    ll = Solution()
    #test data 1
    # houses = [1, 2, 3, 4]
    # heaters = [1, 4]

    #test data 2
    houses = [2, 7, 4, 9, 10, 8]
    heaters = [3, 7, 5]

    #test data 3
    # houses = [1,2,3]
    # heaters = [2]


    x = ll.findRadius(houses, heaters)
    print(x)


