class ListNode:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = key
        self.next = next 

class DataStream:

    def __init__(self):
        self.dummy = ListNode(0)
        self.tail = self.dummy
        self.num_to_prev = {}
        #用self.duplicates来存那些已经出现过的数
        self.duplicates = set()
          
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        #如果这个num已经在duplicates里出现，不用看返回，它不是unique
        if num in self.duplicates:
            return
        
        #如果这个数没有在哈希表里出现，调用push_back函数把它放进哈希表
        if num not in self.num_to_prev:
            self.push_back(num)            
            return
        
        #如果这个数以在哈希表里，将它加入duplicates set中，并在哈希/链表中删了它
        # find duplicate, remove it from hash & linked list
        self.duplicates.add(num)
        self.remove(num)
    
    #删链表中的num
    def remove(self, num):
        #这里的prev是在哈希表里num对应的链表的前继节点，num是哈希表里的key
        prev = self.num_to_prev.get(num)
        #删这个key在哈希表里的值
        del self.num_to_prev[num]
        #删链表中的这个num,
        prev.next = prev.next.next
        #将删完的节点的下个节点的key值连向prev
        if prev.next:
            self.num_to_prev[prev.next.val] = prev
        else:
            # if we removed the tail node, prev will be the new tail
            self.tail = prev

    def push_back(self, num):
        # new num add to the tail
        #让链表的尾节点联上新的ListNode(num)
        self.tail.next = ListNode(num)
        #存这个点在哈希表中，这里的self.tail尾节点是num的前继节点
        self.num_to_prev[num] = self.tail
        #移动尾指针到最后
        self.tail = self.tail.next

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        #这里dummy.next 总是指向first unique number
        if not self.dummy.next:
            return None
        return self.dummy.next.val
if __name__ == '__main__':
    ll = DataStream()
    ll.add(1)
    ll.add(2)
    x = ll.firstUnique()
    print(x)
    ll.add(1)
    y = ll.firstUnique()
    print(y)
  