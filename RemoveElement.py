class Solution:
    def removeElement(self, nums, val):

        # 此题的思想是：把val的直尽量移到数组的右边或数组的最后
        #不是val的值在数组的左边，这样可以知道最后数组有几个数
        #满足条件， 当数组为空是， 返回 0
        if nums is None:
            return 0
        
        #用头尾2个指针，分别指向 0，和数组最后一个元素
        i, last = 0, len(nums)-1
        #当头指针总是小于等于尾指针时， 开始循环
        while i <= last:
            #如果头指针指的数字等于val, 
            if nums[i] == val:
                #头指针指的数和尾指针指的数字进行相交换
                nums[i], nums[last] = nums[last], nums[i]
                #这时候完成一次交换后，尾指针 -1， 向左移动一次
                last -= 1
            else:
                #如果头指针指的数不是val, 这时候移动头指针向右一步
                i += 1
        #因为头尾指针相等的时候，头指针还向右走一步，所以返回i就是
        #前面有几个有效的数字在数组里， 因为数组是从0开始
        return i
    
        #note: 当左右指针重合时，左右指针遍历完数组中的所有的元素
        #这样两个指针在最坏的情况下指遍历数组一次， 
        #时间复杂度O（n), n 为数组的长度，只需最多遍历一次
        #空间复杂度为O（1）， 因为没有额外开数组，只是在原数组上进行
        # in place 交换，所以为 O（1）
        
if __name__ == '__main__':
    ll = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    x = ll.removeElement(nums, val)
    print(x)




