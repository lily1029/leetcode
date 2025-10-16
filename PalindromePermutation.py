class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def can_permute_palindrome(self, s: str) -> bool:
        #初始化一个字典
        s_count = {}

        # 这里count在字典里每一个字母出现的个数
        for c in s:
            s_count[c] = s_count.get(c, 0) + 1
        
        # 这里统计奇数串的长度，如果奇数串大过1，说明它不是一个palindrome
        odd_count = 0

        #go through 每一个字母的个数，看哪些是奇数个，并记录下来
        for count in s_count.values():
            if count % 2 != 0:
                odd_count += 1
        
        #最后返回的是只能有一个多余的字母和偶数的字符串组成palindrome
        return odd_count <= 1

if __name__ =='__main__':
        solution = Solution()
        # s = "code"

        s = "cedec"
        x = solution.can_permute_palindrome(s)
        print(x)


