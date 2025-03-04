class TwoSum(object):

    def __init__(self):
        # initialize your data structure here
        self.count = {}
        
    # Add the number to an internal data structure.
    # @param number {int}
    # @return nothing
    def add(self, number):
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

    # Find if there exists any pair of numbers which sum is equal to the value.
    # @param value {int}
    # @return true if can be found or false
    def find(self, value):
        #go through the count,用value - num 看有没有差在count里，这里要注意是找pair,所以count[num] > 1
        #可以有2个相同数字也算pair, 而且还有一个条件就是value - num != num，是说这个pair的数字不想等时
        for num in self.count:
            #当满足这个条件就返回true, 这里的find花费了O(n) time go through the count
            if value - num in self.count and (value - num != num or self.count[num] > 1):
                return True
        
        #走到这步说明没有这个pair, 返回false
        return False

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)

if __name__ == '__main__':
    ll = TwoSum()
    x = ll.add(1)
    y = ll.add(3)
    z = ll.add(5)
    t = ll.add(5)
    q = ll.find(10)
    w = ll.find(7)
    print(q)
    print(w)
    
    
