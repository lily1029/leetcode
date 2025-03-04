# #这个method, add takes O(1), find takes O(n)
# class TwoSum(object):

#     def __init__(self):
#         # initialize your data structure here
#         self.count = {}
        
#     # Add the number to an internal data structure.
#     # @param number {int}
#     # @return nothing
#     def add(self, number):
#         if number in self.count:
#             self.count[number] += 1
#         else:
#             self.count[number] = 1

#     # Find if there exists any pair of numbers which sum is equal to the value.
#     # @param value {int}
#     # @return true if can be found or false
#     def find(self, value):
#         #go through the count,用value - num 看有没有差在count里，这里要注意是找pair,所以count[num] > 1
#         #可以有2个相同数字也算pair, 而且还有一个条件就是value - num != num，是说这个pair的数字不想等时
#         for num in self.count:
#             #当满足这个条件就返回true, 这里的find花费了O(n) time go through the count
#             if value - num in self.count and (value - num != num or self.count[num] > 1):
#                 return True
        
#         #走到这步说明没有这个pair, 返回false
#         return False


#这个method 是对这道题的 follow up question, if we 
#use less "add" and we use more "find" opertation
#这里find takes O(1)time.
class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        #这里用了一个哈希set，用了额外的空间
        #这个set用于存所有的两数和，以方便find在O(1)时间查找
        self.sum_hash = set()
        #这个structure 存add 进来的数
        self.nums = []

    def add(self, number):
        #go through self.nums 里的每一个数和新进来的相加保存和
        #放入哈希set 里
        for num in self.nums:
            self.sum_hash.add(num + number)
        
        #add进来的放入self.nums
        self.nums.append(number)
        

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        #直接在O（1）时间里找到是不是有2数之和在
        return value in self.sum_hash
if __name__ == '__main__':
    ll = TwoSum()
    x = ll.add(1)
    y = ll.add(3)
    z = ll.add(5)
    q = ll.find(4)
    w = ll.find(7)
    print(q)
    print(w)
    
    
