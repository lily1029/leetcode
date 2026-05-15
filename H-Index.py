class Solution:
    """
    @param citations: a list of integers
    @return: return a integer
    """
    def h_index(self, citations):
        # 论文总数
        n = len(citations)
        # 累计论文数量（从高引用往低统计）
        tot = 0 
        
        #这里counter的作用就是用counter的index number 去记录有index number 的citation有几篇
        #用counter里index number 去记录citations 里文章的数量
        #比如： 【3，0， 6， 1， 5】对有一篇文章有3次citations为
        #     【0， 0， 0， 1， 0， 0】
        # counter[i] 表示引用数恰好为 i 的论文数量
        # counter的大小为 n+1，因为 h-index 最大不超过 n
        #counter的作用,可以统计：how many papers do we have for the same citation ? 
        #later, we consider how many papers do we have for the citation >= n
        counter = [0] * (n+1)
             
        # 遍历每篇论文的引用数
        for c in citations:
            # 如果引用数 >= n，归入最高counter（引用数超过n意义相同）
            if c >= n:
                counter[n] += 1
            else:
                # 否则归入对应的counter,这里是根据c的大小找对应相同的index 在counter里
                counter[c] += 1
        
        #从高到低遍历每个counter（从 n 到 0）,这时候从右往左遍历， 
        #因为知道最右边index 最大，也是citation 数最多的文章有几个
        #这里的i 就是要找的 h-index
        for i in range(n, -1, -1):
            # 累加当前counter里的论文数
            tot += counter[i]
            # 如果累计论文数 >= i，说明找到了 h-index
            #这里的条件tot >= i满足时，说明了满足了h-index的definition从题目中
            #e.g: 这里paper = 3, h= 3,
            if tot >= i:
                # 直接返回 i（满足"至少 i 篇论文各被引用至少 i 次"）
                return i
        
        # 如果没找到，返回 0
        return 0


if __name__ == '__main__':
    ll = Solution()
    citations = [3, 0, 6, 1, 5]
    x = ll.h_index(citations)
    print(x)
   

