class Solution:

    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """

    def sortLetters(self, chars):
        
        # Convert string to a list of characters since strings are immutable in Python
        chars = list(chars)

        # 定义左右指针并初始化
        left = 0
        right = len(chars) - 1

        # 两指针相向移动，交差则结束
        while left <= right:
            # 左指针向右移动，直到找到第一个大写字母
            while left <= right and chars[left].islower():
                left += 1

            # 右指针向左移动，直到找到第一个小写字母
            while left <= right and chars[right].isupper():
                right -= 1

            # 将左边的大写字母和右边的小写字母交换位置
            if left <= right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        
        return ''.join(chars)

if __name__ == '__main__':
    ll = Solution()
    chars = "abAcD"
    x = ll.sortLetters(chars)
    print(x)