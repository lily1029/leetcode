class Solution:
  
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s:
            return 0 
        
        left = 0 
        longest = 0 
        counter = {}
        
        # use right pointer to go through list s 
        for right in range(len(s)):
            # here is to count how many characters appear in s 
            counter[s[right]] = counter.get(s[right], 0) + 1            

            # 这里要判断如果超过了k个字符后，要移动左指针
            # 判断条件是left <= right and 超过k个字符了
            while left <= right and len(counter) > k:
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
    