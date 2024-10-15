class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longest_palindrome(self, s: str) -> int:
        # we define a hash = {} , it is a dictionary, 
        #it has a key and a value
        hash = {}

        #go through the string
        for i in s:
            #如果这个字母出现偶数次，我们删掉它，因为它可以
            #build 有效的palindrome
            if i in hash:
                del hash[i]
            else:
                hash[i] = 'True' #找出只出现一次的字母

        #得到有几个只出现一次的字母
        remove = len(hash)

        #如果出现好几个一次出现的字母，必须都去掉，只留一个build palindrome
        if remove > 0:
            remove = remove - 1
        #最后有效的是整个字符串长度剪去所有多余的单个字母
        return len(s) - remove
if __name__ =='__main__':
        solution = Solution()
        s = "abccccdd"
        x = solution.longest_palindrome(s)
        print(x)
