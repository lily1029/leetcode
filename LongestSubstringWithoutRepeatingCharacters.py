class Solution:
   
    def lengthOfLongestSubstring(self, s):
        # write your code here
        #unique_chars这里面只存不重复的字符
        #并且它被定义为set()
        #e.g unique_chars = {'a','b','c'}
        unique_char = set()
        # j代表右边的指针
        j = 0 
        #获得s串的长度
        n = len(s)
        #全局变量
        longest = 0 
        for i in range(n):
            #右指针向右走的条件是j<n,并且s[j]没有在set()中
            #我们就把右指针指的字符放入set中，并且右指针+1
            while j < n and s[j] not in unique_char:
                unique_char.add(s[j])
                j += 1 

            #当while循环不满足时，我们更新全局变量，这时说明
            #在set里有重复的，我们remove掉左指针指的字符   
            longest = max(longest, j - i)
            unique_char.remove(s[i])
        
        #最后结果返回全局变量最长的 
        return longest
if __name__ == '__main__':
    ll = Solution()
    s = "abcabcbb"
    x = ll.lengthOfLongestSubstring(s)
    print(x)
