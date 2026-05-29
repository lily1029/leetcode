class Solution:
    """
    @param n: an integer
    @return: the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n
    """
    # Method: Two-Pointer(approach)
    def next_greater_element(self, n):
        # 把整数 n 转成字符串再拆成单字符列表，方便逐位读写，
        #例如 230241 -> ['2','3','0','2','4','1']
        a = list(str(n))
        
        # Step_1: find the initial switch
        # i 从倒数第二位开始（最后一位右边没有邻居，无法比较）
        i = len(a) - 2

        # 从右往左找"下降点"：只要当前位 >= 右邻位，
        # 就继续往左挪；停下时 a[i] < a[i+1]
        while i >= 0 and a[i] >= a[i + 1]:
            # 当前位不满足条件（>= 右邻位），指针左移一位
            i -= 1

        # 如果一直挪到 -1 都没找到下降点，说明整个数字是
        # 递减排列，已是最大排列，没有更大的，返回 -1
        if i < 0: 
            return -1

        # j 从最右边开始，准备找一个要和 a[i] 交换的数字
        j = len(a) - 1
        # 从右往左找第一个"严格大于 a[i]"的位置
        # 也就是：（a[j] <= a[i] 就继续左移）
        while j >= 0 and a[j] <= a[i]:
            # 当前 a[j] 不够大，指针左移
            j -= 1
        
        # 交换 a[i] 和 a[j]：用刚好比 a[i] 大一点的数字顶到 i 位，
        # 保证整体只增大最小幅度
        a[i], a[j] = a[j], a[i]

        # Step_2: switch from i + 1 to the end,
        # making the number smaller and smaller 
        # 重置双指针：i 指向后缀起点 (i+1)，j 指向末尾，准备相向反转
        i, j = i + 1, len(a) - 1
        # 双指针相向移动，反转 i 右边的后缀
        #（此时后缀是降序，反转后变升序 = 最小）
        while i < j:
            # 交换左右两端的字符
            a[i], a[j] = a[j], a[i]
            # 左指针右移
            i += 1
            # 右指针左移
            j -= 1
        
        # Step_3: answer 
        # 把字符列表拼回字符串，再转成整数，得到候选答案
        res = int(''.join(a))
        # 用 try/except 包裹溢出判断
        try:
            # 如果结果 >= 2^31
            #（即超过 32 位有符号整数上限 2147483647），抛出异常
            if res >= (1 << 31): 
                raise Exception("too large")
            # 没超界，返回结果
            return res
        # 捕获上面抛出的"too large"异常
        except: 
            # 溢出时返回 -1
            return -1

# 只有直接运行本文件时才执行下面的测试代码（被 import 时不执行）
if __name__ == '__main__':
    # 创建 Solution 实例
    ll = Solution()
    # 设置测试输入
    n = 230241
    # 调用方法求解，结果存入 x
    x = ll.next_greater_element(n)
    # 打印结果（230241 的下一个更大排列是 230412）
    print(x)