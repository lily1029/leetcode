# class Solution:
#     """
#     这道题的做法就是：因为它是rotated sorted array,这个array就分成了2
#     部分，上面一部分，下面一部分，所以分界线条件是 A[mid] >= A[start]在
#     上部分，否则就是分在了下部分，详情请看图
#     """

#     def search(self, A, target):
#         if not A:
#             return -1

#         start, end = 0, len(A) - 1
#         while start + 1 < end:
#             mid = (start + end) // 2
#             # here is the left upper case
#             if A[mid] >= A[start]:
#                 #当是在upper case的情况，target包在start 和mid
#                 #之间，所以end = mid, 丢掉mid右边的部分
#                 if A[start] <= target <= A[mid]:
#                     end = mid
#                 else:
#                     start = mid
#             else:
#                 # this case is right bottom 
#                 #如果target包在mid 和end之间，丢掉mid左边部分（上面部分），
#                 #set start = mid, 然后继续二分查找
#                 if A[mid] <= target <= A[end]:
#                     start = mid
#                 else:
#                     end = mid
                    
#          # here is we have limited only two elements left
#         if A[start] == target:
#             return start
#         if A[end] == target:
#             return end
#         return -1
# if __name__ == '__main__':
#     ll = Solution()
#     A = [4, 5, 1, 2, 3]
#     target = 5
#     x = ll.search(A, target)
#     print(x)

class Solution:
    """
    LintCode 62 · Search in Rotated Sorted Array

    ===== 最关键的思考点：为什么用 A[mid] >= A[start] =====
    1) 旋转有序数组 = "两段各自升序"。左段值偏大、右段值偏小，中间有个"断崖"
       （最大值直接跌到最小值）。例：[4,5,1,2,3] = [4,5] + [1,2,3]。
    2) 数组不是整体有序，所以不能直接拿 A[mid] 和 target 比来决定方向。
    3) 关键事实：无论断崖在哪，[start..mid] 与 [mid..end] 这两半中，
       至少有一半是"完整升序、没被断崖切到"的。
    4) A[mid] >= A[start] 就是用来判断哪一半有序：
         - 成立  -> 从 start 到 mid 没跌崖 -> 左半 [start..mid] 完整升序（mid 在上半段）。
         - 不成立-> 中间跌过崖 -> 断崖在左半 -> 右半 [mid..end] 完整升序（mid 掉到下半段）。
    5) 确定了"有序的那一半"后，才能安全地用区间判断 low <= target <= high
       来决定 target 在不在这半段里——区间判断成立的前提就是这段有序。
    6) 为什么和 A[start] 比：A[start] 是当前窗口的左端点，是稳定参照；拿 mid 和它比，
       等于问"窗口左端到 mid 有没有跨过断崖"，从而定位断崖在左半还是右半。
       （也有模板用 A[mid] 和 A[end] 比，思路对称，同样正确。）
    7) 为什么是 >= 而不是 >：本题元素互不相同，且循环用了 start+1 < end，
       mid 一定严格大于 start，所以 A[mid] 不会等于 A[start]，>= 与 > 在这里等价；
       写 >= 只是把"相等"也归到上半段，属于保险/惯例写法。
    """

    def search(self, A, target):
        # 边界：空数组直接返回 -1，避免后面 len(A)-1 取到 -1 出错
        if not A:
            return -1

        # 双指针圈定查找区间 [start, end]，初始为整个数组
        start, end = 0, len(A) - 1

        # 用 start+1 < end 作为循环条件：当 start 和 end "相邻"时就停，
        # 好处是循环内 mid 永远严格落在 (start, end) 之间，绝不会越界或死循环；
        # 退出后区间里只剩两个元素（start、end），最后单独判断即可。
        while start + 1 < end:
            # 取中点；写成 start + (end - start)//2 可防大数溢出，这里 // 2 已够用
            mid = (start + end) // 2

            # ===== 情况 A：左半 [start..mid] 是完整升序（mid 在"上半段"）=====
            if A[mid] >= A[start]:
                # 左半既然有序，就能用区间判断：target 是否落在 [A[start], A[mid]] 内。
                # 在区间内 -> target 只可能在左半 -> 收右端 end=mid，丢掉 mid 右边。
                if A[start] <= target <= A[mid]:
                    end = mid
                # 不在左半区间 -> target 只能在右半 -> 收左端 start=mid。
                else:
                    start = mid

            # ===== 情况 B：A[mid] < A[start]，右半 [mid..end] 是完整升序（mid 掉到"下半段"）=====
            else:
                # 右半有序，用区间判断：target 是否落在 [A[mid], A[end]] 内。
                # 在区间内 -> target 只可能在右半 -> 收左端 start=mid，丢掉 mid 左边（上半段）。
                if A[mid] <= target <= A[end]:
                    start = mid
                # 不在右半区间 -> target 只能在左半 -> 收右端 end=mid。
                else:
                    end = mid

        # ===== 退出循环：区间内只剩 start、end 两个元素，逐一核对 =====
        # 先看 start 位置是否命中
        if A[start] == target:
            return start
        # 再看 end 位置是否命中
        if A[end] == target:
            return end
        # 两个都不是，说明 target 不存在
        return -1


if __name__ == '__main__':
    # 简单自测
    ll = Solution()
    A = [4, 5, 1, 2, 3]   # 旋转后的数组：左段[4,5] + 右段[1,2,3]
    target = 5
    x = ll.search(A, target)
    print(x)               # 期望输出 1（5 在下标 1）
