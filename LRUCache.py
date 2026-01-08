class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next 

class LRUCache:
    def __init__(self, capacity):
        self.key_to_prev = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity

    #push_back method的作用是在一开始hashtable里没有任何key时，我们往进放新节点
    def push_back(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node 
        self.tail = node 
    
    def pop_front(self):
        # 删除头部
        head = self.dummy.next 
        del self.key_to_prev[head.key]
        self.dummy.next = head.next 
        # Check if there's a next node to update its previous reference
        if head.next: 
            self.key_to_prev[head.next.key] = self.dummy

    #kick method的作用就是把正在访问的在hashtale里对应的值踢到链表尾部,这里
    #链表尾部，表示most recently used(访问的node),总是放在最右边，符合题意
    #这里的 prev来自：get 里self.kick(self.key_to_prev[key])
    #self.key_to_prev[key] = prev, prev 是linkedlist 上key对应的前继节点  
    #将数据移动至尾部
    def kick(self, prev):
        #先用node 固定prev.next 节点，其实就是key对应的节点
        node = prev.next 
        if node == self.tail:
            return 
        
        #remove the current node from linkedlist
        prev.next = node.next 
        # Check if there's a next node to update its previous reference
        if node.next:  
            self.key_to_prev[node.next.key] = prev
        node.next = None 
        #然后在把这个node节点作为一个独立节点用push_back函数接到链表尾巴上
        self.push_back(node)
    
    # @return an integer,key就是cache提供的，可以是个字符串，也可以是个整数..
    #获取数据
    def get(self, key): 
        #如果key不再哈希表里，就返回-1
        if key not in self.key_to_prev:
            return -1 
        self.kick(self.key_to_prev[key])
        return self.key_to_prev[key].next.value

    #数据放入缓存 
    def set(self, key, value):
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            #这里有个地方判断链表的最后一个节点值是不是等于想设置的value值
            #如果是，就返回True,并return，不用走剩下的code, 因为在kick 里已经在链表末尾
            #链接了这个设置的value值的node，这里想检验一下，不用走多余的剩下的code
            self.key_to_prev[key].next.value = value
            return 
        
        #如果key不存在，则存入新节点
        self.push_back(LinkedNode(key, value))
        #如果缓存超出上限
        if len(self.key_to_prev) > self.capacity:
            #删除头部
            self.pop_front()

    def print_cache(self):
        current = self.dummy.next
        while current is not None:
            print(f'({current.key}, {current.value})', end=" -> ")
            current = current.next
        print("None")

if __name__ == '__main__':
    ll = LRUCache(2)
    ll.set(2, 0)
    # print(ll.get(2))
    # ll.print_cache()
    ll.set(3, 5)
    # ll.get(2)
    # print(ll.get(2))
    # ll.get(3)
    # print(ll.get(3))
    # ll.get(4)
    # print(ll.get(4))
    ll.set(4, 1)
    ll.set(3, 5)
    print(ll.get(3))
    ll.print_cache()
    ll.get(4)
    ll.print_cache()
    # ll.get(4)
    # ll.get(3)
    # ll.print_cache()





