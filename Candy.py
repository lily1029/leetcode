class Solution:
    # @param ratings, a list of integer
    # @return an integer

    def candy(self, ratings):
        #每个小孩都分一颗糖果, 即设定一个全1的 count 数组.
        # candynum = [ 1, 1, 1]
        candynum = [1 for i in range(len(ratings))]

        #然后开始遍历这个数组，先从左向右，如果发现一个小孩的左边的小孩的糖果数比
        #自己低，，那么这个小孩的糖果数 = 他左边孩子的糖果数 + 1
        for i in range(1, len(ratings)):
            #如果发现这个小孩的糖果数比左边的孩子糖果数高
            if ratings[i] > ratings[i-1]:
                #那么这个小孩的糖果数 = 他左边孩子的糖果数 + 1
                candynum[i] = candynum[i-1] + 1

        #从右往左遍历一次
        for i in range(len(ratings)-2, -1, -1):
            #这里要注意：如果右边的孩子的糖果数比自己低，并且右边的孩子的糖果数是大于等于
            #我的糖果数时，这时我的糖果数等于右边孩子糖果数 + 1 
            if ratings[i+1] < ratings[i] and candynum[i+1] >= candynum[i]:
                #我的糖果数时，这时我的糖果数等于右边孩子糖果数 + 1
                candynum[i] = candynum[i+1] + 1

        #最后返回所有糖果数
        return sum(candynum)
    
if __name__ == '__main__':
    ll = Solution()  # Fixed typo here
    ratings = [1, 0, 2]
    x = ll.candy(ratings)
    
    print(x)  # Call the method and print the result
