class LoadBalancer:
    
    def __init__(self):
        #进去的server id
        self.server_ids = []
        #用这个hashmap 记录server 和这个server 在array中的地方
        #self.server_ids = [1, 2]
        #self.id2index = {1: 0, 2: 1}
        self.id2index = {}
    #此题做法和lintcode 657完全一样，都是用一个array 和一个hash map完成    
    # @param {int} server_id add a new server to the cluster 
    # @return nothing
    def add(self, server_id):
        if server_id in self.id2index:
            return
        
        self.server_ids.append(server_id)
        self.id2index[server_id] = len(self.server_ids) - 1
     
    # @param {int} server_id remove a bad server from the cluster
    # @return nothing
    def remove(self, server_id):
        #如果在哈希表里没有这个server_id, 就return
        if server_id not in self.id2index:
            return
        
        index = self.id2index[server_id]
        del self.id2index[server_id]
        
        #1.拿到数组中最后一个数值. 2将最后一个数值放入哈希表=要删数的index
        #3.将要删的数在数组中覆盖成最后一个数 4.把数组中最后一个数弹出
        last_server_id = self.server_ids[-1]
        self.id2index[last_server_id] = index
        self.server_ids[index] = last_server_id
        self.server_ids.pop()

    # @return {int} pick a server in the cluster randomly with equal probability
    def pick(self):
        import random 
        index = random.randint(0, len(self.server_ids) - 1)
        return self.server_ids[index]

if __name__ == '__main__':
    ll = LoadBalancer()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    print(ll.pick())
    print(ll.pick())
    print(ll.pick())
    ll.remove(1)
    print(ll.pick())
    print(ll.pick())
    print(ll.pick())
    


