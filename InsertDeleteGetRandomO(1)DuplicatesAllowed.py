import random
import collections
class RandomizedCollection:
    def __init__(self):
        #初始化一个数组，一个dictionary
        # e.g insert(1), insert(1), insert(2)
        #self.vals: [1, 1, 2]
        #self.indexs: defaultdict(<class 'set'>, {1:{0, 1}})
        #self.indexs : {1:{0, 1}, 2: {2}}
        self.vals, self.indexs = [], collections.defaultdict(set)
        
    def insert(self, val):
        #将要插入的数val直接append到数组中
        #self.vals: [1, 1, 2]
        self.vals.append(val)

        #在dictionary中记录数组出现的位置
        #self.indexs : {1:{0, 1}, 2: {2}}
        self.indexs[val].add(len(self.vals)-1)
        #这里判断是第一次insert,长度为1，返回true
        #第二次insert,长度变化，返回false,因为
        #第一次已经插入了，返回false
        return len(self.indexs[val]) == 1
    
    def remove(self, val):
		#1.获取要删的数在字典中最先出现的位置，也是在array最左边的位置
        #这里可以用pop() method
        #2.在数组中将x位置赋值为None
        #3.return True 
        #如果此数不再dictionary里，返回False
        if not self.indexs[val]:
            return False
        
        # x 可以获取要删的这个数的最左边的位置 {0, 1}, x = 0
        #e.g: self.indexs[val] = {0, 1},  romove(1)
        #e.g: self.indexs[1] = {1}, x = 0
        x = self.indexs[val].pop()
        
        #在数组中将这个要删的数的位置赋值为None
        #self.vals = [None, 1, 2]
        self.vals[x] = None
        #这里返回true, 表示已经删除了这个数（e.g val  = 1）
        return True

    def getRandom(self):
        x = None
        while x is None:
            #这里调用random()函数，从self.vals选一个
            x = random.choice(self.vals)
        return x

if __name__ == '__main__':
    obj = RandomizedCollection()
    param = obj.insert(1)
    param = obj.insert(1)
    param = obj.insert(2)
    x = obj.getRandom()
    print(x)
    param = obj.remove(1)
   
    y = obj.getRandom()
    print(y)
