import random
class RandomizedSet:
    
    def __init__(self):
        # do intialization if necessary
        self.nums, self.pos = [], {}
    

    """
    此题如果想在O(1)时间内完成insert, remove, getrandom,我们必须用一个数组（list/array）和一个
    哈希表共同完成，insert 的数字在list中的位置是哈希的value, key 就是这个insert 数的值
    e.g self.nums=[1, 2] self.pos = {1:0, 2:1}
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if val in self.pos:
            return False
        
        #在这里得到hash的value
        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1 
        return True 

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val not in self.pos:
            return False 
        # idx是要删的这个数在哈希表中的位置，last 是数组中最后一个数
        idx, last = self.pos[val], self.nums[-1]
        
        #把要删的那个数用最后一个数覆盖掉，idx是要删的这个数在哈希表中的位置
        #，也就是数组中原始位置
        #把最后一个数在哈希表中的位置换成要删除数的位置
        self.nums[idx], self.pos[last] = last, idx
        self.nums.pop()
        del self.pos[val]
        return True 
        

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        return self.nums[random.randint(0, len(self.nums) -1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
if __name__ == '__main__':
    obj = RandomizedSet()
    param = obj.insert(1)
    param = obj.remove(2)
    param = obj.insert(2)
    x = obj.getRandom()
    print(x)
    param = obj.remove(1)
    param = obj.insert(2)
    y = obj.getRandom()
    print(y)

