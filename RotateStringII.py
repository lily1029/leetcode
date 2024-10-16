class Solution:
    """
    @param str: An array of char
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """
    def rotate_string2(self, str: str, left: int, right: int) -> str:
        #计算总偏移量   
        offset = left - right
        #计算出总的偏移量多少
        offset %= len(str)

        # 2 means offset [2: ] means 2 后面的所有char, 包括2位置的char
        #[ :2] means 2 前面的所有chars, 但是不包括2所在位置的char
        return str[offset : ] + str[ : offset]
if __name__ =='__main__':
        solution = Solution()
        s = "abcdefg"
        left = 3
        right = 1
        x = solution.rotate_string2(s, left, right)
        print(x)
