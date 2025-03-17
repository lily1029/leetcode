class Solution:
    
    #同向双指针，此题的做法就是：一次遍历即可，遍历的同时记录
    #每个字母出现的次数和当前子串中不同字母的长度。其中定义一个
    #左指针记录左边界，当前的子串即左边界到遍历位置对应的子串长度
    #如果不同字母的个数超过k,则向右调整左边界（左指针向右移),
    #遍历同时维护最长子串的长度即可
    def lengthOfLongestSubstringKDistinct(self, s, k):

        if not s:
            return 0 
        
        #左指针
        left = 0 
        #全局变量，算最终结果，最长的k distinct characters
        longest = 0 
        #用counter算每个字母出现过几次，
        counter = {}
        
        #这里是右指针 to go through list s 
        for right in range(len(s)):
            # here is to count how many characters appear in s 
            counter[s[right]] = counter.get(s[right], 0) + 1            

            # 这里要判断如果超过了k个字符后，要移动左指针
            # 判断条件是left <= right and 超过k个字符了
            while left <= right and len(counter) > k:
                #这里因为超过了k,所以调整左指针，去掉一个左边的字母，如果归0，
                #就delete 掉左边的字母，从下个子串算维持 k个distinct chars
                #所以left + 1 
                counter[s[left]] -= 1 
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1 
            
            # update 字符串的总长度
            longest = max(longest, right - left + 1)
        return longest
if __name__ == '__main__':
    ll = Solution()
    s = "eceba"
    k = 3
    x = ll.lengthOfLongestSubstringKDistinct(s, k)
    y = print(x)
    

