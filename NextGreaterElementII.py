import collections

class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        result = [-1] * n       # 初始化结果数组，默认 -1
        mono_stack = []              # 单调栈，存的是索引

        # 遍历两倍长度，模拟循环数组
        for i in range(2 * n):
            # 当栈不为空，且当前元素大于栈顶索引对应的元素
            while mono_stack and nums[mono_stack[-1]] < nums[i % n]:
                idx = mono_stack.pop()           # 取出栈顶索引
                result[idx] = nums[i % n]  # 找到了它的下一个更大元素
            if i < n:
                mono_stack.append(i)
                print(f"i={i}, stack={mono_stack}")

        return result

if __name__ == '__main__':
    ll = Solution()
    nums = [1, 2, 3, 4, 3]
    x = ll.nextGreaterElements(nums)
    print(x)  # 预期输出：[2, 3, 4, -1, 4]