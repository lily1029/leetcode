class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
       #write your code
       if not pages:
           return 0

       #这里二分复印的时间 
       start, end = max(pages), sum(pages)
       
       while start + 1 < end:
           mid = (start + end) // 2 
           
           if self.get_least_people(pages, mid) <= k:
               ##可以复制完
               end = mid
           else:
               start = mid
       #二分到最后还要看下边界条件，在start时间里是否
       #也可以复制完书，如果不可以， 就是end时间
       if self.get_least_people(pages, start) <= k:
           return start
       return end 
             
    #此函数算在time_limit时，要几个人复印
    def get_least_people(self, pages, time_limit):
        #需要的人数
        count = 1 
        time_cost = 0 
        for page in pages:
            if page + time_cost > time_limit:
                count += 1 
                time_cost = page
            else:
                time_cost += page
        return count
if __name__ =='__main__':
    ll = Solution()
    pages = [3, 2, 4]
    k = 2
    x = ll.copyBooks(pages, k)
    print(x)


