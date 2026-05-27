import collections
class Solution:
    #这个题的做法是：遍历两遍数组模拟循环，用单调栈记录
    #还没找到答案的索引，一旦遇到更大的元素就更新结果
    def nextGreaterElements(self, nums):
        #得到数组长度
        n = len(nums)
        # 初始化结果数组，默认 -1
        result = [-1] * n  
        # 单调栈，存的是数组的index    
        mono_stack = []              

        # 遍历两倍长度，模拟循环数组
        for i in range(2 * n):
            # 当栈不为空，且当前元素(nums[i % n])大于栈顶index对应的元素
            while mono_stack and nums[mono_stack[-1]] < nums[i % n]:
                # 取出栈顶index
                idx = mono_stack.pop()  
                # 找到了它的下一个更大元素,并且更新到result数组里       
                result[idx] = nums[i % n]  
            
            #让index进入stack，等待找到下一个更大的元素
            if i < n:
                mono_stack.append(i)
                print(f"i={i}, stack={mono_stack}")

        return result

if __name__ == '__main__':
    ll = Solution()
    nums = [1, 2, 3, 4, 3]
    x = ll.nextGreaterElements(nums)
    print(x)  # 预期输出：[2, 3, 4, -1, 4]