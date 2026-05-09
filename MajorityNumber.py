class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Boyer-Moore 是一个非常聪明的算法，
        #专门用来找数组中的多数元素（出现次
        #数超过一半的数）
        #核心思想：把不同的数字互相抵消，最后
        #剩下的就是多数元素！因为多数元素出现
        #次数超过一半，所以就算被其他所有数字
        #抵消，最后还是会剩下它。

        #程序最初始，设置当前最多元素为0
        current_major = 0
        #设置它的count 次数为0
        count = 0
        
        #go through 整个array 一次
        for num in nums:
            #当count 为0时，
            if count == 0:
                #设置最多元素为这个num
                current_major = num
            
            #当count不为0时，有多个最多元素时
            if num == current_major:
                #统计它的个数，放到count里
                count += 1
            else:
                #这里是不同元素相互抵消的部分
                #当go through arry时出现
                #新的元素和最多元素不同时，
                #新的元素抵消掉一个最多元素的数量1
                count -= 1
        
        #最后返回的一定是那个出现次数最多的元素
        # time: O(n) , space: O(1)
        return current_major

if __name__ == '__main__':
    ll = Solution()
    # nums = [3, 2, 3]
    nums = [2,2,1,1,1,2,2]
    x = ll.majorityElement(nums)
    print(x)

    



