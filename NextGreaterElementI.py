class Solution:
    def next_greater_element(self, nums1, nums2):
        #这道题的做法是遍历 nums2,在遍历的过程中，使用stack
        #记录每个数字的下一最大数字，然后重新遍历nums1根据
        #hashmap 里的结果给出答案
        # 用栈来追踪还没找到下一个更大元素的数字
        stack = []
        # 用哈希表存储每个数字对应的下一个更大元素
        # key = 当前数字, value = 下一个更大的数字
        # hashmap = {key : value}
        # e.g nums1 = [4, 1, 2] nums2 = [1, 3, 4,2]
        #hashmap = {1:3, 3:4} -> 是根据nums2得来的
        hashmap = {}

        # 遍历nums2中的每个数字
        for num in nums2:
            # 如果栈不为空，并且当前数字比栈顶元素大
            # 说明找到了栈顶元素的"下一个更大元素"
            while stack and num > stack[-1]:
                # 把栈顶元素弹出，并记录它的下一个更大元素
                hashmap[stack.pop()] = num
            # 把当前数字压入栈，等待找到它的下一个更大元素
            stack.append(num)

        # 遍历nums1，从哈希表中查找每个数字的下一个更大元素
        # 如果找不到（即栈中剩余元素），返回-1
        return [hashmap.get(i, -1) for i in nums1]
        
if __name__ == '__main__':
    ll = Solution()
    nums1 = [4,1,2] 
    nums2 = [1,3,4,2]
    x = ll.next_greater_element(nums1, nums2)
    print(x)